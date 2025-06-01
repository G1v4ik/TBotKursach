from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.api import crud
from bot.fsm.forms_fsm import FormResponse
from bot.bot import bot_support

callback_router = Router()

@callback_router.callback_query(
    F.data.startswith('response:')
)
async def callback_response(call: CallbackQuery,
                            state: FSMContext):
    
    data = call.data.replace('response:', '')
    data = data.split(":")
    id_message, username, telegram_id = data[0], data[1], data[2]

    await state.set_state(FormResponse.id_message)
    await state.update_data(id_message=id_message)
    await state.set_state(FormResponse.telegram_id_user)
    await state.update_data(telegram_id_user=telegram_id)
    
    await state.set_state(FormResponse.message)
    await call.message.answer("Введите ответ")


@callback_router.message(
    F.text, FormResponse.message
)
async def send_response(message: Message, state: FSMContext):
    await state.update_data(message=message.text)
    response_data = await state.get_data()
    await state.set_state(None)
    await state.clear()

    await bot_support.send_message(
        response_data['telegram_id_user'],
        (
        f"<b>ответ по вашему вопросу:</b>\n"
        f"{response_data['message']}"
        )
    )

    await crud.response_support_message(
        response_data['id_message'])
