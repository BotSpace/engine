# app/engine/flow_controller.py

import logging
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, Update

from .fsm import FlowState
from .loader import SchemaLoader
from .executors import NodeExecutor
from .state_manager import StateManager

class FlowController:
    def __init__(self, bot: Bot, schema_path: str):
        self.bot = bot
        self.schema = SchemaLoader(schema_path)
        self.executor = NodeExecutor(bot)
        self.logger = logging.getLogger(self.__class__.__name__)

    async def handle_update(self, event: Message | CallbackQuery, fsm_context: FSMContext):
        state_manager = StateManager(fsm_context)
        current_state = await fsm_context.get_state()
        
        # --- XATO TUZATILGAN QISM ---
        # Ob'ekt tipini `isinstance` yordamida tekshiramiz
        chat_id = None
        if isinstance(event, Message):
            chat_id = event.chat.id
        elif isinstance(event, CallbackQuery):
            chat_id = event.message.chat.id

        if chat_id is None:
            self.logger.warning(f"Update turidan chat_id aniqlanmadi: {type(event)}")
            return
        # --- TUZATISH TUGADI ---

        self.logger.info(f"CHAT_ID={chat_id}: Yangi event qabul qilindi. Holat: {current_state}")

        if current_state == FlowState.waiting_for_trigger:
            node_id_to_check = await state_manager.get_waiting_node_id()
            trigger_node = self.schema.get_node(node_id_to_check)
            
            if trigger_node and self._check_trigger(trigger_node, event):
                self.logger.info(f"CHAT_ID={chat_id}: Kutilgan trigger ({node_id_to_check}) ishga tushdi.")
                await fsm_context.clear()
                await self._traverse(trigger_node, chat_id, fsm_context)
            else:
                self.logger.debug(f"CHAT_ID={chat_id}: Event kutilgan triggerga ({node_id_to_check}) mos kelmadi.")
        else:
            for trigger_node in self.schema.root_triggers:
                if self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})")
                    await self._traverse(trigger_node, chat_id, fsm_context)
                    return

    async def _traverse(self, trigger_node: dict, chat_id: int, fsm_context: FSMContext):
        state_manager = StateManager(fsm_context)
        # Boshlang'ich nuqta - triggerdan keyingi node'lar
        nodes_to_process = self.schema.get_next_nodes(trigger_node['id'])

        while nodes_to_process:
            node = nodes_to_process.pop(0)
            node_type = node.get('type', '')
            
            if 'Trigger' in node_type:
                self.logger.info(f"CHAT_ID={chat_id}: To'xtab, triggerni kutmoqdamiz (ID: {node['id']})")
                await state_manager.set_wait_for_trigger(node['id'])
                return
            
            elif 'Node' in node_type:
                await self.executor.execute(node, chat_id)
                nodes_to_process.extend(self.schema.get_next_nodes(node['id']))
        
        self.logger.info(f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda.")
        await state_manager.clear_state()

        
    def _check_trigger(self, trigger_node: dict, event: Message | CallbackQuery) -> bool:
        data, node_type = trigger_node.get('data', {}), trigger_node.get('type')
        
        # --- 1-holat: MessageTriggerNode (matn, kontakt, lokatsiya va hk uchun) ---
        if node_type == 'MessageTriggerNode' and isinstance(event, Message):
            # Trigger qanday kontent turini kutayotganini aniqlaymiz
            expected_content_type = data.get('type') # 'text', 'contact', 'location'

            # 1a: Matn kutilganda (buyruq yoki oddiy matn)
            if expected_content_type == 'text' and event.text:
                filter_type = data.get('filter') # 'command', 'any'
                if filter_type == 'command':
                    expected_command = data.get('context', {}).get('value')
                    return event.text == expected_command
                elif filter_type == 'any':
                    return True # Har qanday matn kelsa, True

            # 1b: Kontakt kutilganda
            elif expected_content_type == 'contact' and event.contact:
                return True # Har qanday kontakt kelsa, True

            # 1c: Lokatsiya kutilganda
            elif expected_content_type == 'location' and event.location:
                return True # Har qanday lokatsiya kelsa, True

        # --- 2-holat: ReplyButtonTriggerNode (FAQAT matnli tugmalar uchun) ---
        elif node_type == 'ReplyButtonTriggerNode' and isinstance(event, Message) and event.text:
            # Trigger qaysi matn(lar)ni kutayotganini aniqlaymiz
            expected_buttons = data.get('selectedButtons', [])
            # Kelgan matn kutilayotgan matnlar ro'yxatida bo'lsa, True
            return event.text in expected_buttons
        
        # --- 3-holat: CallbackQueryTriggerNode (inline tugmalar uchun) ---
        # Kelajakda to'ldiriladi
        elif node_type in ['CallbackButtonTriggerNode', 'CallbackQueryTriggerNode'] and isinstance(event, CallbackQuery):
            # Bu yerda `event.data` ni tekshirish logikasi bo'ladi
            pass

        # Agar hech qaysi shart bajarilmasa
        return False
