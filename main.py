from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Я помогу тебе найти учебные программы с оплатой и кредитами 🎓")

if __name__ == "__main__":
    executor.start_polling(dp)
