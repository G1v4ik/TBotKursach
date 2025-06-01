from aiogram.fsm.state import State, StatesGroup

class FormQuestion(StatesGroup):
    telegram_id = State()
    username = State()
    message = State()


class FormResponse(StatesGroup):
    id_message = State()
    telegram_id_user = State()
    message = State()

