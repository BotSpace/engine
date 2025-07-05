# app/engine/node_executor.py
import logging
from aiogram import Bot
from typing import Dict, Any
from app.engine.utils import build_keyboard

class NodeExecutor:
    """Berilgan node'ning amalini bajarish uchun mas'ul."""

    def __init__(self, bot: Bot):
        self.bot = bot
        # Har bir Action node turi uchun alohida metod
        self._handlers = {
            "SendTextMessageNode": self._execute_send_text,
            "SendPhotoNode": self._execute_send_photo,
            # ... boshqa action turlari uchun metodlar ...
        }

    async def execute(self, node: Dict, chat_id: int):
        node_type = node.get('type')
        handler = self._handlers.get(node_type)
        if handler:
            logging.info(f"CHAT_ID={chat_id}: Bajarilmoqda -> {node_type} (ID: {node['id']})")
            await handler(node.get('data', {}), chat_id)
        else:
            logging.warning(f"CHAT_ID={chat_id}: {node_type} uchun bajaruvchi topilmadi. O'tkazib yuborildi.")

    # --- Action Handler Metodlari ---
    
    async def _execute_send_text(self, data: Dict[str, Any], chat_id: int):
        text = data.get('messageText', '[Matn topilmadi]')
        buttons = data.get('buttons')
        # Bu yerda `disable_web_page_preview`, `parse_mode` kabilarni ham
        # `data` dan olib, `send_message`ga uzatish mumkin.
        await self.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=build_keyboard(buttons)
        )
        
    async def _execute_send_photo(self, data: Dict[str, Any], chat_id: int):
        # photoSourceType ga qarab file_id yoki url ishlatiladi.
        photo_id = data.get('photoFileId') or data.get('photoUrl')
        if not photo_id:
            logging.error("SendPhotoNode uchun photoFileId yoki photoUrl topilmadi.")
            return

        caption = data.get('caption', '')
        buttons = data.get('buttons')
        await self.bot.send_photo(
            chat_id=chat_id,
            photo=photo_id,
            caption=caption,
            reply_markup=build_keyboard(buttons)
        )