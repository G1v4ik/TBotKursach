from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton 
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, \
    InlineKeyboardBuilder


from bot.tools.Tool import UserTool


import json


msg = UserTool()


def kb_start():
    kb = ReplyKeyboardBuilder()

    kb.button(
        text=msg.user_keyboard['kb_start']['student']
    )

    kb.button(
        text=msg.user_keyboard['kb_start']['teacher']
    )
    return kb.adjust(1,1).as_markup()