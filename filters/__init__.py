from aiogram import Dispatcher

from init import dp
from .is_admin import IsAdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsAdminFilter)
