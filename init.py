from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

logger.add(
    'logs/all.log',
    rotation='10MB',
    compression='zip',
    backtrace=True,
    diagnose=True,
    level='INFO')

logger.add(
    'logs/err.log',
    rotation='10MB',
    compression='zip',
    backtrace=True,
    diagnose=True,
    level='ERROR')

if not config.BOT_TOKEN:
    exit("Token is not exist")

# init
storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
