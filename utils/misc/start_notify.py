from loguru import logger

from aiogram import Dispatcher
from config import ADMIN_ID

@logger.catch()
async def on_startup_notify(dp: Dispatcher):
    logger.info('Bot started!')
    await dp.bot.send_message(ADMIN_ID, 'Bot started!')
