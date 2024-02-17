import asyncio
import logging
from aiogram import Bot, Dispatcher
from command_handlers import command_router, api_router, message_router
from config import BOT_TOKEN
from aiogram.enums import ParseMode
from aiogram.types import BotCommand


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

    await bot.set_my_commands(commands=[
        BotCommand(command='start', description="start/restart bot"),
        BotCommand(command='help', description="Manual for this bot"),
        BotCommand(command='all', description="This command for get all cources"),
        BotCommand(command='usd', description="Dollar"),
        BotCommand(command='eur', description="Yevro"),
        BotCommand(command='rub', description="Rubl")
    ])
    dp = Dispatcher()
    
    dp.include_routers(command_router, api_router, message_router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
