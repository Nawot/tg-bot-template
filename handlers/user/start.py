from init import dp
from loguru import logger
from aiogram import types

from utils.misc import rate_limit


@dp.message_handler(commands=['start'])
@rate_limit(5, 'start')
@logger.catch()
async def send_welcome(message: types.Message):
    await message.reply('Hi!')
