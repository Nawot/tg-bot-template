from init import dp
from loguru import logger
from aiogram import types

from utils.misc import rate_limit


@dp.message_handler(commands=['help'])
@rate_limit(5, 'help')
@logger.catch()
async def send_help(message: types.Message):
    await message.reply('Help coming!')
