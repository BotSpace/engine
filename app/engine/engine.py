# app/engine/engine.py

import logging
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from .loader import SchemaLoader
from .triggers import TriggerFinder
from .executors import NodeExecutor
# Hali yaratilmagan, lekin kelajak uchun reja
# from .navigator import FlowNavigator
# from .context import ExecutionContext

class FlowEngine:
    def __init__(self, bot: Bot, flow_file_path: str):
        self.bot = bot
        # 1. Sxemani yuklaymiz
        schema = SchemaLoader(flow_file_path)
        self.nodes = schema.nodes
        self.edges = schema.edges

        # 2. Yordamchi komponentlarni yaratamiz
        self.trigger_finder = TriggerFinder(list(self.nodes.values()))
        self.node_executor = NodeExecutor(bot)
        # self.navigator = FlowNavigator(self.edges) # Kelajakda

    async def handle_message(self, message: Message):
        """Kiruvchi xabarga ishlov beradi."""
        start_node = self.trigger_finder.find_for_message(message)
        if start_node:
            await self._traverse_flow(start_node, message.chat.id)
        else:
            logging.warning(f"Message uchun trigger topilmadi: '{message.text}'")

    async def handle_callback(self, callback: CallbackQuery):
        """Kiruvchi callback'ga ishlov beradi."""
        start_node = self.trigger_finder.find_for_callback(callback)
        if start_node:
            await callback.answer()
            await self._traverse_flow(start_node, callback.message.chat.id)
        else:
            logging.warning(f"Callback uchun trigger topilmadi: '{callback.data}'")
            await callback.answer("Bu tugma uchun amal topilmadi.", show_alert=True)

    async def _traverse_flow(self, current_node: dict, chat_id: int):
        """Sxema bo'ylab yuradi (hozircha shartsiz)."""
        while current_node:
            await self.node_executor.execute(current_node, chat_id)

            # --- KELAJAKDA BU QISM FlowNavigator'ga O'TADI ---
            outgoing_edges = self.edges.get(current_node['id'], [])
            if not outgoing_edges:
                logging.info(f"Sxema tugadi (ID: {current_node['id']}).")
                break

            # Hozircha faqat birinchi yo'nalish
            next_edge = outgoing_edges[0]
            current_node = self.nodes.get(next_edge['target'])
            if not current_node:
                logging.error(f"Target node topilmadi: {next_edge.get('target')}")
                break