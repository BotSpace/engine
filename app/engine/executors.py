# app/engine/executors.py

import logging
from typing import Dict
from aiogram import Bot
from aiogram.types import ReplyKeyboardRemove
# Yordamchi keyboard builder'ni ham alohida modulga chiqaramiz
from .utils import build_keyboard

class NodeExecutionError(Exception):
    pass

class NodeExecutor:
    def __init__(self, bot: Bot):
        self.bot = bot
        # Kelajakda bu yerga boshqa turdagi node'lar uchun "handler"lar qo'shiladi
        self._handlers = {
            'SendTextMessageNode': self._handle_send_text_message
        }

    async def execute(self, node: Dict, chat_id: int):
        """Node'ni uning turiga qarab bajaradi."""
        node_type = node.get('type')
        handler = self._handlers.get(node_type)

        if not handler:
            logging.warning(f"Node turi uchun bajaruvchi (handler) topilmadi: {node_type}")
            return

        try:
            logging.info(f"Bajarilmoqda: Node ID {node.get('id')}, Turi: {node_type}")
            await handler(node.get('data', {}), chat_id)
        except Exception as e:
            raise NodeExecutionError(f"Node {node.get('id')} bajarilishida xatolik: {e}")

    # --- HANDLER METODLARI ---
    # Har bir handler faqat o'ziga kerakli 'data' va 'chat_id' ni oladi
    async def _handle_send_text_message(self, data: Dict, chat_id: int):
        """SendTextMessageNode uchun logikani bajaradi."""
        text_to_send = data.get('messageText', '[Xabar matni topilmadi]')

        if 'buttons' in data and not data['buttons']:
            keyboard = ReplyKeyboardRemove()
        else:
            keyboard = build_keyboard(data.get('buttons')) # utils.py dan chaqiramiz

        await self.bot.send_message(
            chat_id=chat_id,
            text=text_to_send,
            reply_markup=keyboard
        )

# Yordamchi funksiyalarni utils.py ga chiqaramiz
# app/engine/utils.py
# ... _build_keyboard funksiyasining kodi shu yerda bo'ladi ...