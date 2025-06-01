from aiogram.utils.keyboard import InlineKeyboardBuilder


def resposnser_kb(username, id_message, telegram_id):
    kb = InlineKeyboardBuilder()
    kb.button(
        text="Ответить", 
        callback_data=f'response:{id_message}:{username}:{telegram_id}'
    )
    return kb.adjust(1).as_markup()
