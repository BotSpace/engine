import logging
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from fastapi import FastAPI

from app.engine.engine import FlowEngine  # FlowEngine import
from app.handlers import router as bot_router  # Router import
from env import BOT_TOKEN, FLOW_FILE_PATH  # Token va flow fayl yo'li

# --- Webhook Sozlamalari ---
BASE_WEBHOOK_URL = (
    "https://8cb464c23649.ngrok-free.app"  # O'zingizning manzilingizni kiriting
)
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"
# ----------------------------

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Ilova ishga tushmoqda...")

    try:
        # Bot va dvigatelni yaratish
        bot = Bot(token=BOT_TOKEN)
        engine = FlowEngine(bot=bot, flow_file_path=FLOW_FILE_PATH)

        # Dispatcher yaratish, engine ni 'engine' kaliti bilan uzatish
        dp = Dispatcher(storage=MemoryStorage(), engine=engine)
        dp.include_router(bot_router)

        # Holatga saqlash
        app.state.bot = bot
        app.state.dispatcher = dp

        # Webhook o‘rnatish
        await bot.set_webhook(url=WEBHOOK_URL)
        logging.info(f"Webhook o'rnatildi: {WEBHOOK_URL}")

        yield  # Ilova ishida davom etish

    except Exception as e:
        logging.critical(f"Kritik xato, ilova ishga tushmadi: {e}", exc_info=True)
        yield  # Xato bo‘lsa ham finally qismiga o‘tadi

    finally:
        logging.info("Ilova to'xtamoqda...")
        if hasattr(app.state, "bot") and app.state.bot:
            await app.state.bot.delete_webhook()
            await app.state.bot.session.close()
            logging.info("Webhook o'chirildi va sessiya yopildi.")


app = FastAPI(lifespan=lifespan)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    dp = app.state.dispatcher
    bot = app.state.bot

    telegram_update = types.Update(**update)
    try:
        await dp.feed_update(bot=bot, update=telegram_update)
    except Exception as e:
        logging.error(f"Update'ni qayta ishlashda xatolik: {e}", exc_info=True)

    return {"status": "ok"}
