import os
import asyncio
from aiogram import Bot, Dispatcher, types
from app.handlers import router

# Token of your telegram-bot
token = os.getenv('TOKEN')

# Initialization of Bot
bot = Bot(token=token)
dp = Dispatcher()


# Async function for start the bot
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


# You know, what it is...
if __name__ == '__main__':
    try:
        print('Bot is running...')
        asyncio.run(main())
    except:
        print('Connection end.')