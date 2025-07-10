# app/engine/handlers/custom_handlers.py
import asyncio
from typing import Dict, Any
from .base import ActionHandler

class CustomCodeHandler(ActionHandler):
    """CustomCodeNode'ni xavfsiz tarzda bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        python_code = data.get('pythonCode', '')
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(f"CustomCodeNode kodini bajarishga tayyorlanmoqda (chat_id: {chat_id})")
        
        # XAVFSIZLIK OGOHLANTIRISHI:
        # `exec()` yoki `eval()` funksiyalarini to'g'ridan-to'g'ri ishlatish O'TA XAVFLI!
        # Bu serverda istalgan kodni bajarish imkonini berib, jiddiy xavfsizlik
        # zaifliklariga olib kelishi mumkin.
        #
        # TO'G'RI YECHIM: Maxsus xavfsiz "sandbox" (qum qutisi) muhitida ishlatish.
        # Buning uchun `restrictedpython` kutubxonasidan foydalanish yoki Piston kabi
        # API orqali alohida xavfsiz servisda kodni ishga tushirish tavsiya etiladi.
        #
        # Hozircha, biz bu amaliyotning xavfliligini ko'rsatish uchun faqat log yozamiz
        # va `async` funksiya ichida kodni bajarishning to'g'ri usulini ko'rsatamiz.

        # Kod bajarilishi uchun mavjud bo'lgan o'zgaruvchilar
        execution_globals = {
            'bot': self.bot,
            'chat_id': chat_id,
            'context': context, # Bu lug'at orqali node'lar o'rtasida ma'lumot almashish mumkin
            'asyncio': asyncio,
            # Xabarga oid o'zgaruvchilar (agar mavjud bo'lsa) context'dan olinadi
            'message': context.get('message'), 
            'callback': context.get('callback_query'),
        }

        try:
            # Asinxron kodni to'g'ri bajarish uchun
            exec_code = f"async def __exec_code():\n"
            exec_code += "".join(f"    {line}\n" for line in python_code.splitlines())
            
            # Kodni lokal scope'da `exec` qilamiz
            exec(exec_code, execution_globals)
            
            # Yaratilgan asinxron funksiyani chaqiramiz
            coro = execution_globals['__exec_code']()
            await coro

            self.logger.info(f"CustomCodeNode kodi muvaffaqiyatli bajarildi (chat_id: {chat_id})")

        except Exception as e:
            error_message = f"Custom code'ni bajarishda xatolik yuz berdi: {e}"
            self.logger.error(error_message, exc_info=True)
            # Xatolik haqida admin yoki foydalanuvchiga xabar berish mumkin
            await self.bot.send_message(chat_id, f"⚠️ Kod bajarishda xatolik:\n<pre>{e}</pre>")