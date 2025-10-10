# app/engine/flow_controller.py

import logging
import re
from typing import Dict, Any

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from geopy.distance import geodesic # pip install geopy

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

    def _check_radius(self, event_location, radius_context: Dict[str, Any]) -> bool:
        """Berilgan nuqta belgilangan radius ichidaligini tekshiradi."""
        try:
            center_lat = float(radius_context.get("lat"))
            center_lng = float(radius_context.get("lng"))
            radius_km = float(radius_context.get("km"))
            user_location = (event_location.latitude, event_location.longitude)
            center_point = (center_lat, center_lng)
            distance = geodesic(user_location, center_point).kilometers
            self.logger.debug(f"Radius tekshiruvi: Masofa {distance:.2f}km, Talab {radius_km}km.")
            return distance <= radius_km
        except (ValueError, TypeError, AttributeError):
            self.logger.warning(f"Radius uchun noto'g'ri qiymatlar keldi: {radius_context}")
            return False

    async def handle_update(
        self, event: Message | CallbackQuery, fsm_context: FSMContext
    ):
        state_manager = StateManager(fsm_context)
        current_state = await fsm_context.get_state()
        flow_context = await fsm_context.get_data()

        chat_id = event.chat.id if isinstance(event, Message) else event.message.chat.id
        
        if isinstance(event, Message):
            flow_context['message'] = event
        elif isinstance(event, CallbackQuery):
            flow_context['callback_query'] = event

        self.logger.info(f"CHAT_ID={chat_id}: Event qabul qilindi. Holat: {current_state}")

        if current_state == FlowState.waiting_for_trigger:
            paused_node_id = await state_manager.get_paused_node_id()
            if not paused_node_id:
                self.logger.warning(f"CHAT_ID={chat_id}: Holat 'waiting' lekin 'paused_node_id' topilmadi. Holat tozalanmoqda.")
                await state_manager.clear_state()
                return

            possible_next_nodes = self.schema.get_next_nodes(paused_node_id)
            for trigger_node in possible_next_nodes:
                if "Trigger" in trigger_node.get("type", "") and self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Kutilgan trigger ({trigger_node['id']}) ishga tushdi.")
                    await self._traverse(trigger_node, chat_id, fsm_context, flow_context, return_to_node_id=paused_node_id)
                    return
            self.logger.debug(f"CHAT_ID={chat_id}: Event kutilgan triggerlarga mos kelmadi.")
        else:
            for trigger_node in self.schema.root_triggers:
                if self._check_trigger(trigger_node, event):
                    self.logger.info(f"CHAT_ID={chat_id}: Yangi ssenariy boshlandi (Root Trigger: {trigger_node['id']})")
                    await self._traverse(trigger_node, chat_id, fsm_context, flow_context)
                    return

    async def _traverse(self, start_node: dict, chat_id: int, fsm_context: FSMContext, flow_context: dict, return_to_node_id: str | None = None):
        state_manager = StateManager(fsm_context)
        nodes_to_process = [start_node]
        last_processed_node_id = start_node["id"]

        while nodes_to_process:
            current_node = nodes_to_process.pop(0)
            node_type = current_node.get("type", "")

            if "Node" in node_type and "Trigger" not in node_type:
                await self.executor.execute(current_node, chat_id, flow_context)
                last_processed_node_id = current_node["id"]
            
            next_nodes = self.schema.get_next_nodes(current_node["id"])

            if not next_nodes:
                continue

            if all("Trigger" in n.get("type", "") for n in next_nodes):
                self.logger.info(f"CHAT_ID={chat_id}: Harakat bajarildi ({last_processed_node_id}), trigger(lar)ni kutish uchun pauza.")
                await state_manager.set_pause_after_node(last_processed_node_id, flow_context)
                return

            nodes_to_process.extend(next_nodes)

        if return_to_node_id:
            self.logger.info(f"CHAT_ID={chat_id}: Harakatlar shoxi tugadi. Avvalgi kutish holatiga qaytilmoqda (Node ID: {return_to_node_id}).")
            await state_manager.set_pause_after_node(return_to_node_id, flow_context)
        else:
            self.logger.info(f"CHAT_ID={chat_id}: Ssenariy shoxi tugadi. Holat tozalanmoqda.")
            await state_manager.clear_state()

    def _check_trigger(self, trigger_node: dict, event: Message | CallbackQuery) -> bool:
        """Trigger shartlarini tekshiruvchi asosiy funksiya."""
        node_type = trigger_node.get("type")
        data = trigger_node.get("data", {})
        
        if node_type == "CommandTriggerNode" and isinstance(event, Message):
            command = data.get("command")
            if not command or not event.text:
                return False
            return event.text.startswith(command)
        
        if node_type == "MessageTriggerNode" and isinstance(event, Message):
            expected_type = data.get("type")
            
            if expected_type and expected_type != "any" and expected_type != event.content_type:
                return False

            filt = data.get("filter")
            context = data.get("context", {})

            if not filt or filt == "any":
                return True

            if filt in ["equals", "contains", "starts_with", "regex", "command"]:
                if not event.text: return False
                value = context.get("value")
                if value is None: return False
                
                if filt == "equals": return event.text == value
                if filt == "contains": return value in event.text
                if filt in ["starts_with", "command"]: return event.text.startswith(value)
                if filt == "regex":
                    try:
                        return bool(re.match(value, event.text))
                    except re.error:
                        self.logger.warning(f"Noto'g'ri regex pattern: {value}")
                        return False
            
            if filt == "radius":
                if not event.location or not context.get("radius"): return False
                return self._check_radius(event.location, context["radius"])

            if filt == "extension":
                if not event.document or not event.document.file_name: return False
                value = context.get("value", "").lower().lstrip('.')
                if not value: return False
                return event.document.file_name.lower().endswith(f".{value}")

            if filt == "size":
                file_size_bytes = 0
                if event.photo: file_size_bytes = event.photo[-1].file_size
                elif event.video: file_size_bytes = event.video.file_size
                elif event.audio: file_size_bytes = event.audio.file_size
                elif event.document: file_size_bytes = event.document.file_size
                
                if file_size_bytes == 0: return False

                try:
                    size_context = context.get("size", {})
                    min_mb_str = size_context.get("min")
                    max_mb_str = size_context.get("max")
                    file_size_mb = file_size_bytes / (1024 * 1024)

                    if min_mb_str and file_size_mb < float(min_mb_str): return False
                    if max_mb_str and file_size_mb > float(max_mb_str): return False
                    return True
                except (ValueError, TypeError):
                    self.logger.warning(f"Fayl hajmi uchun noto'g'ri qiymatlar: {context.get('size')}")
                    return False
            
            return False

        elif node_type == "ReplyButtonTriggerNode" and isinstance(event, Message):
            selected_button: dict | None = data.get("selectedButton")
            if not selected_button: return False
            btn_type, btn_text = selected_button.get("type"), selected_button.get("text")
            
            if btn_type == "reply" and event.text == btn_text: return True
            if btn_type == "request_contact" and event.contact: return True
            if btn_type == "request_location" and event.location: return True
            return False

        elif node_type in ["CallbackButtonTriggerNode", "CallbackQueryTriggerNode"] and isinstance(event, CallbackQuery):
            if not event.data: return False
            
            if node_type == "CallbackButtonTriggerNode":
                selected_callbacks = data.get("selectedCallbacks", [])
                return event.data in selected_callbacks
            
            if node_type == "CallbackQueryTriggerNode":
                filt, value = data.get("filter"), data.get("context", {}).get("value")
                if filt == "any": return True
                if not filt or not value: return False
                
                if filt == "equals": return event.data == value
                if filt == "contains": return value in event.data
                if filt == "starts_with": return event.data.startswith(value)
                if filt == "regex":
                    try:
                        return bool(re.match(value, event.data))
                    except re.error:
                        return False
            return False
        
        return False