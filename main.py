import asyncio

from aiogram import Dispatcher

from aiogram.methods import DeleteWebhook

from bot.routers import include_routers

from bot.bot import bot_support


dp = Dispatcher()


async def main():
   
    await bot_support(
        DeleteWebhook(drop_pending_updates=True)
        )
    
    await include_routers(dp=dp)

    await dp.start_polling(bot_support)


if __name__ == "__main__":
    try:
        print ("bot is running...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot is stopped...')