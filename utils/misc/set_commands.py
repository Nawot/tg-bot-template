from aiogram import types

async def set_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Help special for you"),
        ]
    )
