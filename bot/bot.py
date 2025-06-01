from os import getenv
from dotenv import load_dotenv

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


load_dotenv()

TOKEN = getenv("TokenBot")

bot_support = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
            )
        )

