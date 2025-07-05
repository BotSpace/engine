# app/handlers.py (TO'G'RILANGAN KOD)

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from app.engine.engine import FlowEngine # <--- To'g'ri klassni import qilamiz

router = Router()

@router.message()
async def universal_message_handler(message: Message, engine: FlowEngine): # <--- MUHIM O'ZGARISH
    """Barcha kiruvchi xabarlarni qabul qilib, dvijokka uzatadi."""
    await engine.handle_message(message)

@router.callback_query()
async def universal_callback_handler(callback: CallbackQuery, engine: FlowEngine): # <--- MUHIM O'ZGARISH
    """Barcha kiruvchi callback'larni qabul qilib, dvijokka uzatadi."""
    await engine.handle_callback(callback)