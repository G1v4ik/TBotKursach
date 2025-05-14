from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from bot.tools.Tool import UserTools
from bot.handlers.user import router_handler_user

@router_handler_user.message(
        StateFilter(None),
)
async def fsm_reg_user(
        message = Message,
        state = FSMContext, 
        user = 'student' or 'teacher'):
    await message.answer(
        text= UserTools.user_answer['msg_reg_student'] if user == 'student' else UserTools.user_answer['msg_reg_teacher']
    )