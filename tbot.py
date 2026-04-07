import asyncio
import os
from dotenv import load_dotenv

from aiogram import Dispatcher, types, Bot, F
from aiogram.filters import Command

load_dotenv()


dp = Dispatcher()

g_buttons = [
        [types.KeyboardButton(text = 'Игра 🎮'), 
        types.KeyboardButton(text = 'Фильм 🎥')],
        [types.KeyboardButton(text = 'О боте 🤖')]
    ]

keyboard = types.ReplyKeyboardMarkup(keyboard=g_buttons, resize_keyboard=True)

@dp.message(Command('start'))
async def test_start(message: types.Message):
    await message.answer('Что хотите найти?', reply_markup=keyboard)

@dp.message(F.text.lower() == 'Привет')
async def echo_handler(message: types.Message) -> None:
    await message.answer(f'Здравствуй, {message.from_user.first_name}!\n\nДоступные команды:\n /start — Описание бота\n /funcs — Функции бота\n\nЧтобы начать работу, выбери, что хочешь найти: игру или фильм', reply_markup=keyboard)

@dp.message(F.text == 'Фильм 🎥')
async def echo_handler(message: types.Message) -> None:
    await message.answer(f'Выдача фильма')

async def main():
    bot = Bot(token = os.getenv("BOT_TOKEN"))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())