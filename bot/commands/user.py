from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.fsm.fsm_user_reg import fsm_reg_user

from bot.tools.Tool import UserTools

router_user_command = Router()

@router_user_command.message(Command('reg'))
async def cmd_reg_user(message: Message, command: CommandObject):
    commands_args = command.args
    print (commands_args)
    if commands_args:
        await fsm_reg_user(user=str(commands_args))
    
    else:
        await message.answer(
            text=UserTools.user_answer['msg_reg_err']
        )