from aiogram.fsm.state import State, StatesGroup


class FormCreateNewUser(StatesGroup):
    telegram_id = State()
    name = State()
    surname = State()
    contact_phone = State()
