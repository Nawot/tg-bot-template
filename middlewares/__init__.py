from aiogram import Dispatcher
from init import dp

from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())