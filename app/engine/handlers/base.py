import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Union, Optional

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Bu funksiya sizning utils.py faylingizda deb hisoblaymiz
from app.engine.utils import build_keyboard

class ActionHandler(ABC):
    """
    Barcha Action Node handler'lari uchun abstrakt baza klassi (interfeys).
    Har bir handler shu klassdan meros oladi va o'zining `handle` metodini implementatsiya qiladi.
    Bu Liskov Substitution Principle (SOLID'ning 'L' harfi) uchun muhim.
    """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def handle(self, data: Dict[str, Any], chat_id: int):
        """
        Har bir handler ushbu metodni o'ziga xos tarzda implementatsiya qilishi SHART.
        :param data: Node'ning `data` maydonidagi ma'lumotlar.
        :param chat_id: Xabar yuboriladigan chat ID.
        """
        raise NotImplementedError

    def _prepare_common_params(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ko'pchilik `send_*` metodlari uchun umumiy bo'lgan parametrlarni tayyorlaydi.
        Bu kod takrorlanishining oldini oladi (DRY tamoyili).
        """
        buttons: Optional[list[list[dict]]] = data.get('buttons')
        
        # `build_keyboard` funksiyasi ReplyKeyboardRemove qaytarishi mumkin,
        # shuning uchun reply_markup None bo'lmasligi kerak
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]] = build_keyboard(buttons)
        
        params = {}
        if reply_markup is not None:
            params['reply_markup'] = reply_markup

        if data.get('disableNotification'):
            params['disable_notification'] = True
        
        if data.get('protectContent'):
            params['protect_content'] = True
            
        return params