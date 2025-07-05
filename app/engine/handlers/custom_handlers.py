# app/engine/executors/custom_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class CustomCodeHandler(ActionHandler):
    """CustomCodeNode'ni xavfsiz tarzda bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        python_code = data.get('pythonCode', '')
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(f"CustomCodeNode'ning kodini bajarishga harakat qilinmoqda (chat_id: {chat_id})")
        
        # DIQQAT: `exec()` funksiyasini to'g'ridan-to'g'ri ishlatish O'TA XAVFLI!
        # Bu yerda maxsus xavfsiz "sandbox" (qum qutisi) muhiti yaratish kerak.
        # Buning uchun restrictedpython, Piston API kabi kutubxonalardan foydalanish mumkin.
        # Hozircha, biz bu amaliyotning xavfliligini ko'rsatish uchun faqat log yozamiz.
        
        self.logger.critical("XAVFSIZLIK OGOHLANTIRISHI: Custom code execution (exec) implementatsiya qilinmagan.")
        # Misol:
        # try:
        #     # Sandbox'da kodni bajarish logikasi...
        # except Exception as e:
        #     self.logger.error(f"Custom code'ni bajarishda xatolik: {e}")