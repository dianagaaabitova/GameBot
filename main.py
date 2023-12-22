from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils import executor

import config

bot = Bot(token=config.telegram_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

url = 'https://maxizhukov.github.io/telegram_game_front'
gameName = "BrainStorm"


@dp.message_handler(commands=['start'])
async def start_dialog(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Начать игру', callback_data='startGame')
    markup.row(button1)

    await bot.send_message(chat_id=message.chat.id, text="Привет!", reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'startGame')
async def startGame(call: types.CallbackQuery):
    await bot.send_game(chat_id=call.message.chat.id, game_short_name=gameName)


@dp.callback_query_handler(lambda callback_query: callback_query. game_short_name == gameName)
async def game(call):
    await bot.answer_callback_query(callback_query_id = call.id, url = url)


async def on_startup(_):
    await dp.start_polling(bot)


# Запускаем бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
