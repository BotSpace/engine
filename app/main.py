# app/main.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from env import BASE_WEBHOOK_URL, BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as common_router

# --- Webhook Sozlamalari ---
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"

print(f"🔍 ~  ~ app/main.py:16 ~ {WEBHOOK_URL}:");

# ----------------------------

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    default_properties = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(token=BOT_TOKEN, default=default_properties)
    controller = FlowController(bot=bot, schema_path=FLOW_FILE_PATH)
    dp = Dispatcher(storage=MemoryStorage(), controller=controller)
    dp.include_router(common_router)
    app.state.bot = bot
    app.state.dispatcher = dp
    await bot.set_webhook(url=WEBHOOK_URL)
    logging.info(f"Webhook o'rnatildi: {WEBHOOK_URL}")
    yield
    logging.info("Webhook o'chirilmoqda...")
    await bot.delete_webhook()
    await bot.session.close()


# ---- MUHIM QATOR ----
# Uvicorn aynan shu "app" nomli o'zgaruvchini qidiradi
app = FastAPI(lifespan=lifespan)
# --------------------


@app.get("/")
async def welcome():
    return {"message": "Welcome to the Bot API!"}


@app.post(WEBHOOK_PATH)
async def bot_webhook(request: Request):
    dispatcher: Dispatcher = request.app.state.dispatcher
    bot: Bot = request.app.state.bot
    update = types.Update(**(await request.json()))
    await dispatcher.feed_update(bot=bot, update=update)
    return {"status": "ok"}