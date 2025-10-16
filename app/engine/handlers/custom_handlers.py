# app/engine/handlers/custom_handlers.py
import asyncio
from typing import Dict, Any

from app.repository import query
from .base import ActionHandler


class CustomCodeHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        python_code = data.get("pythonCode", "")
        if not python_code:
            self.logger.warning("CustomCodeNode'da bajarish uchun kod yo'q.")
            return

        self.logger.info(
            f"CustomCodeNode kodini bajarishga tayyorlanmoqda (chat_id: {chat_id})"
        )

        execution_globals = {
            "bot": self.bot,
            "query": query,
            "chat_id": chat_id,
            "context": context,
            "asyncio": asyncio,
            "message": context.get("message"),
            "callback": context.get("callback_query"),
        }

        try:
            exec_code = f"async def __exec_code():\n"
            exec_code += "".join(f"    {line}\n" for line in python_code.splitlines())
            exec(exec_code, execution_globals)
            coro = execution_globals["__exec_code"]()
            await coro
            self.logger.info(
                f"CustomCodeNode kodi muvaffaqiyatli bajarildi (chat_id: {chat_id})"
            )
        except Exception as e:
            error_message = f"Custom code'ni bajarishda xatolik yuz berdi: {e}"
            self.logger.error(error_message, exc_info=True)
            await self.bot.send_message(
                chat_id, f"⚠️ Kod bajarishda xatolik:\n<pre>{e}</pre>"
            )

