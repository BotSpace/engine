import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from engine import FlowExecutor

# --- SOZLAMALAR ---
# O'zingizning bot tokeningizni shu yerga qo'ying
BOT_TOKEN = "8058205725:AAHiWbWdDl5jnwj_Eqz3NWY8m2itKATkkc8" 
FLOW_FILE_PATH = "flow.json"
# ------------------

# Logger sozlamalari
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    # Bot va Dispatcher obyektlarini yaratamiz
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # JSON faylini o'qiymiz
    try:
        with open(FLOW_FILE_PATH, 'r') as f:
            flow_data = json.load(f)
        logging.info(f"'{FLOW_FILE_PATH}' fayli muvaffaqiyatli o'qildi.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"'{FLOW_FILE_PATH}' faylini o'qishda xatolik: {e}")
        return

    # Dvijok yadrosini yaratamiz
    executor = FlowExecutor(flow_data=flow_data, bot_instance=bot)

    # Barcha xabarlarni ushlab oladigan universal handler
    @dp.message()
    async def universal_handler(message: types.Message):
        """Barcha xabarlarni dvijokka yuboradi."""
        await executor.start_flow_from_message(message)

    # Universal handler'ni ro'yxatdan o'tkazamiz
    # Bu qismni main() ichiga olgan ma'qul, global scope'da qoldirmasdan
    dp.message.register(universal_handler)


    # Polling'ni boshlaymiz
    try:
        logging.info("Bot ishga tushmoqda...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())