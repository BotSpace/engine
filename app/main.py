import asyncio
import logging
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from env import BOT_TOKEN, FLOW_FILE_PATH
from app.engine.flow_controller import FlowController
from app.handlers.common import router as bot_router

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main() -> None:
    logging.info("Ilova ishga tushmoqda (polling rejim)...")

    bot: Optional[Bot] = None
    try:
        default_properties = DefaultBotProperties(parse_mode="HTML")
        bot = Bot(token=str(BOT_TOKEN), default=default_properties)
        controller = FlowController(bot=bot, schema_path=FLOW_FILE_PATH)

        dp = Dispatcher(storage=MemoryStorage(), controller=controller)
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
