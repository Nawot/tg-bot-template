from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
import config


class IsAdminFilter(BoundFilter):
    """
    Simple filter for check than message from admin. 
    """
    
    async def check(self, message: types.Message):
        return message.from_user.id == config.ADMIN