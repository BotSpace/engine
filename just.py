import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

# Keyboard with a button
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Press me!", callback_data="button_pressed")]
])

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Hello! Press the button or send me a message.", reply_markup=keyboard)

@dp.callback_query()
async def button_handler(callback: types.CallbackQuery):
    await callback.answer("Button pressed!")
    await callback.message.answer("You pressed the button!")

@dp.message()
async def message_handler(message: types.Message):
    await message.reply(f"You said: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)