from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

import config

bot = Bot(token=config.telegram_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(_):
    await dp.start_polling(bot)


# Запускаем бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
