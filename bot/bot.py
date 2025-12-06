import os, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
WEBAPP_URL = os.getenv("TG_WEBAPP_URL")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="Open planner", web_app=types.WebAppInfo(url=WEBAPP_URL)))
    await msg.answer("Открой планировщик:", reply_markup=kb)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())