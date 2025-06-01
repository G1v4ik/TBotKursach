import json

from aiogram import Router, F
from aiogram.filters import (
    Command, 
    CommandObject,
    CommandStart
)
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.schames import schames
from bot.api import crud
from bot import config
from bot.fsm.forms_fsm import FormQuestion
from bot.keyboards.user import resposnser_kb


router_user_command = Router()


@router_user_command.message(CommandStart())
async def cmd_start(message: Message):
    text = """
Привет, я бот помошник. 
Я могу:

/q - здесь вы можете задать любой вопрос по
    автошколе

/help - полный список команд

"""
    await message.answer(text)

@router_user_command.message(Command('help'))
async def cmd_help(message: Message):
    text = (
        "<b><i>[Список всех команд]</i>\n"
        "/q - задать любой вопрос по автошколе\n"
        "/url - ссылка на сайт\n"
        "/code - ссылка на github\n"
        "/qresponse - ответить на сообщения\n"
        "/contact - контакты тех.поддержки\n"
        "/help - [<i>вы тут</i>]</b>"
    )
    await message.answer(text)


@router_user_command.message(Command('contact'))
async def cmd_contact(message: Message):
    await message.answer("https://t.me/Forgithe")


@router_user_command.message(Command('url'))
async def cmd_url(message: Message):
    await message.answer(config.URL_SITE)


@router_user_command.message(Command("code"))
async def cmd_code(message: Message):
    await message.answer(config.URL_GITHUB)


@router_user_command.message(Command("qresponse"))
async def cmd_question_admin(messages: Message):
    list_support_messages = await crud.get_list_support_message()
    for i in list_support_messages:
        await messages.answer(
            f"{i.username}\n{i.message}",
            reply_markup=resposnser_kb(
                i.username, 
                i.id_message,
                i.telegram_id)
        )

@router_user_command.message(Command("q"))
async def cmd_question(
    message: Message, 
    state: FSMContext
):
    await state.set_state(FormQuestion.telegram_id)
    await state.update_data(
        telegram_id=message.from_user.id
    )
    await state.set_state(FormQuestion.username)
    await state.update_data(
        username=message.from_user.username
    )
    await state.set_state(FormQuestion.message)
    await message.answer("Введите своё сообщение: ")


@router_user_command.message(F.text, FormQuestion.message)
async def process_message(
    message: Message, 
    state: FSMContext
):
    await state.update_data(message=message.text.lower())
    message_question = await state.get_data()
    await state.set_state(None)
    send = await crud.send_support_message_from_user(data=schames.DS_support_new_message.model_validate_json(json.dumps(message_question)))
    await state.clear()
    if send.status_code == 200:
        await message.answer("OK: Сообщение успешно доставлено")
    
    else:
        await message.answer("Err: Ошибка, попробуйте позже")