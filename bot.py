import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8111573248:AAHkpx3F8KLY8EOSumPJgqvMo4g5Lrn74s4"

# Логтарды қосу
logging.basicConfig(level=logging.INFO)

# Бот пен диспетчерді жасау
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Старт командасы
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Сәлем! Мен сенің Telegram ботыңмын! 🚀")

# Ботты іске қосу
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
