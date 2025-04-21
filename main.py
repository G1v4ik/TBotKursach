from os import getenv
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.methods import DeleteWebhook

from bot.routers import include_routers


load_dotenv()

TOKEN = getenv("TokenBot")


dp = Dispatcher()


async def main():
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
            )
        )

    await bot(
        DeleteWebhook(drop_pending_updates=True)
        )
    
    await include_routers(dp=dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
