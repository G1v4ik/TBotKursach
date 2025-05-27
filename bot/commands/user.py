from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.tools.Tool import UserTools
from bot.schames.schames import RegUserType

from pydantic import ValidationError

router_user_command = Router()

@router_user_command.message(Command('reg'))
async def cmd_reg_user(message: Message, command: CommandObject):
    commands_args = command.args
    
    if commands_args:
        try:
            RegUserType(user_type=commands_args.lower())

        except ValueError as ve:
            await message.answer("Либо student, либо teacher")

    else:
        await message.answer(
            text=UserTools.user_answer['msg_reg_err']
        )