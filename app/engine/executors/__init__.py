# app/engine/executors/__init__.py
import logging
from aiogram import Bot
from typing import Dict, Any, Type

from app.engine.handlers.base import ActionHandler
from app.engine.handlers.custom_handlers import CustomCodeHandler
from app.engine.handlers.media_handlers import SendAudioHandler, SendFileHandler, SendPhotoHandler, SendVideoHandler
from app.engine.handlers.message_handlers import SendTextHandler

class NodeExecutor:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)
        self._handlers: Dict[str, Type[ActionHandler]] = {
            "SendTextMessageNode": SendTextHandler,
            "SendPhotoNode": SendPhotoHandler,
            "SendVideoNode": SendVideoHandler,
            "SendAudioNode": SendAudioHandler,
            "SendFileNode": SendFileHandler,
            "CustomCodeNode": CustomCodeHandler,
        }

    async def execute(self, node: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        node_type = node.get('type')
        handler_class = self._handlers.get(node_type)
        if not handler_class:
            self.logger.warning(f"Node turi uchun bajaruvchi (handler) topilmadi: {node_type}")
            return
        try:
            handler_instance = handler_class(self.bot)
            await handler_instance.handle(node.get('data', {}), chat_id, context)
            self.logger.info(f"Node (ID: {node.get('id')}) muvaffaqiyatli bajarildi.")
        except Exception as e:
            self.logger.error(f"Node (ID: {node.get('id')}, Turi: {node_type}) bajarilishida kutilmagan xatolik: {e}", exc_info=True)