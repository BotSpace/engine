import asyncio
import logging
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_TOKEN, FLOW_FILE_PATH
from app.engine.engine import FlowEngine
from app.handlers import router as bot_router

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main() -> None:
    logging.info("Ilova ishga tushmoqda (polling rejim)...")

    bot: Optional[Bot] = None
    try:
        bot = Bot(token=BOT_TOKEN)
        engine = FlowEngine(bot=bot, flow_file_path=FLOW_FILE_PATH)

        dp = Dispatcher(storage=MemoryStorage(), engine=engine)
        dp.include_router(bot_router)

        await dp.start_polling(bot)

    except asyncio.CancelledError:
        logging.info("Polling bekor qilindi.")
        raise
    except Exception as exc:
        logging.critical(f"Kritik xato: {exc}", exc_info=True)
    finally:
        if bot is not None:
            try:
                await bot.session.close()
                logging.info("Bot sessiyasi yopildi.")
            except Exception as e:
                logging.warning(f"Bot sessiyasini yopishda xatolik: {e}", exc_info=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Ilova to'xtatildi (user interrupt).")
