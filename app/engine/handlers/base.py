# app/engine/handlers/base.py
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List

from aiogram import Bot
from app.engine.utils import build_keyboard

class ActionHandler(ABC):
    """
    Barcha Action Node handler'lari uchun abstrakt baza klassi (interfeys).
    """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        """
        Har bir handler ushbu metodni o'ziga xos tarzda implementatsiya qilishi SHART.
        :param data: Node'ning `data` maydonidagi ma'lumotlar.
        :param chat_id: Xabar yuboriladigan chat ID.
        :param context: Sxema bo'ylab yuradigan umumiy ma'lumotlar lug'ati.
        """
        raise NotImplementedError

    def _prepare_common_params(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ko'pchilik `send_*` metodlari uchun umumiy bo'lgan parametrlarni tayyorlaydi.
        """
        params = {}
        
        # Yangi `build_keyboard` funksiyasiga butun konfiguratsiyani uzatamiz
        reply_markup = build_keyboard(data.get('keyboard'))
        if reply_markup:
            params['reply_markup'] = reply_markup

        if data.get('disableNotification'):
            params['disable_notification'] = True
        
        if data.get('protectContent'):
            params['protect_content'] = True
            
        return params

    def _get_recipients(self, data: Dict[str, Any], initial_chat_id: int) -> List[int]:
        """Qabul qiluvchilar ro'yxatini shakllantiradi."""
        recipients_config = data.get('recipients', {})
        ids = []
        
        if recipients_config.get('sendToSender', True):
            ids.append(initial_chat_id)
            
        additional_ids_str = recipients_config.get('additionalIds', [])
        for user_id in additional_ids_str:
            try:
                ids.append(int(user_id))
            except (ValueError, TypeError):
                self.logger.warning(f"Qo'shimcha qabul qiluvchi ID'si noto'g'ri formatda: {user_id}")
        
        # Dublikatlarni olib tashlaymiz
        return list(set(ids))