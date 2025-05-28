import json

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.fsm.Forms import FormCreateNewUser
from bot.api import crud
from bot.schames import schames

form_router = Router()

async def user_is_register(message, state):
    
    if await crud.get_user_by_tg_id_or_None(
        message.from_user.id
    ) is not None:
        return True


async def user_isnt_reg_or_err(message):
    if await crud.is_user_reg(message.from_user.id):
        try:
            raise ValueError
        except ValueError:
            await message.answer('вы зарегестрированы')



@form_router.message(Command('reg'))
async def new_user(message: Message, state: FSMContext) -> None:

    await user_isnt_reg_or_err(message)

    text = """
Укажите имя, фамилию и номер телефона
Пример:
Иван 
Иванов 
89990001122
"""
    
    await state.set_state(FormCreateNewUser.telegram_id)
    await state.update_data(telegram_id=message.from_user.id)
    await state.set_state(FormCreateNewUser.name)
    await message.answer(text)

@form_router.message(Command('cancel'))
@form_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        "Отмена регистрации"
    )

@form_router.message(Command('ok'))
@form_router.message(F.text.casefold() == "ok")
async def process_confirmation(message: Message, state: FSMContext) -> None:
    data_user = await state.get_data()

    
    await crud.registration_user(
        schames.DS_UserSchames.model_validate_json(json.dumps(data_user))
    )
    
    await message.answer(f"Ваш аккаунт зарегистрирован с данными: <b>{data_user['name']} {data_user['surname']} {data_user['contact_phone']}</b>")

    await state.clear()

@form_router.message(F.text, FormCreateNewUser.name)
async def process_name_user(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text.lower())
    await state.set_state(FormCreateNewUser.surname)
    await message.answer('Введите фамилию')


@form_router.message(F.text, FormCreateNewUser.surname)
async def process_surname_user(message: Message, state: FSMContext) -> None:
    await state.update_data(surname=message.text.lower())
    await state.set_state(FormCreateNewUser.contact_phone)
    await message.answer('Введите номер телефона (89991112233)')


@form_router.message(F.text, FormCreateNewUser.contact_phone)
async def process_contact_phone_user(message: Message, state: FSMContext) -> None:
    await state.update_data(contact_phone=message.text.lower())
    await state.set_state(None)
    data_user = await state.get_data()

    text = f"""
Ваши данные: 
<b>{data_user['name']} {data_user['surname']} {data_user['contact_phone']}</b>
Если допустили ошибку, 
то отмените операцию /cancel or cancel 
и начните заново
Если все верно то введите /ok"""

    await message.answer(text)

