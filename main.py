from aiogram import executor, types, Dispatcher
from init import dp
from loguru import logger
import middlewares, filters, handlers
from utils.misc.start_notify import on_startup_notify
from utils.misc.set_commands import set_commands


async def on_startup(dp: Dispatcher):
    await set_commands(dp)
    await on_startup_notify(dp)


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    main()
