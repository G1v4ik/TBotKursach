from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from bot.tools.Tool import UserTools

router_handler_user = Router()


@router_handler_user.message(Command('start'))
async def start_message(message: Message):
    await message.answer(UserTools.user_answer['msg_start'])