import json

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.methods.get_chat import GetChat

from pydantic import ValidationError

from bot.tools.Tool import UserTools
from bot.schames import schames

from bot.api import crud


router_user_command = Router()

async def user_is_reg_or_err(message):
    if not await crud.is_user_reg(message.from_user.id):
        try:
            raise ValueError
        except ValueError:
            await message.answer('вы не зарегестрированы')


async def user_isnt_reg_or_err(message):
    if await crud.is_user_reg(message.from_user.id):
        try:
            raise ValueError
        except ValueError:
            await message.answer('вы зарегестрированы')


    
@router_user_command.message(Command('start'))
async def start_message(message: Message):
    text = """
<b>Привет!</b> 👋

Я — ваш помошник от сайта <s>pressf-drivingschool</s>
Моя задача — сделать ваше взаимодействие с этим приложением более удобным и интересным. 

Для полного списка команд

<b>/help</b>

"""

    await message.answer(text)


@router_user_command.message(Command('help'))
async def cmd_help(message: Message, command: CommandObject):
    text="""
<b>/contact - связь с поддержкой
/reg - для регистрации
/groups - для плучения списка групп
/groupscreate [title] - создать группу
/groupsjoin [id group] - вступить в группу</b>
"""

    await message.answer(text)


@router_user_command.message(Command('contact'))
async def cmd_contact(message: Message):
    await message.answer("<a>https://t.me/Forgithe</a>")

@router_user_command.message(Command('groups'))
async def cmd_groups(message: Message):
    await user_is_reg_or_err(message)
    text = f"""
<b>Список Групп по теории\n
[id] | [title] | [*]\n
* - Вы в этой группе</b>\n
"""
# {[f" * <b>{i.id_grouplearn} | {i.title}</b>\n" for i in await crud.get_list_groupslearns()]}

    user_in_group_learn = await crud.get_groups_by_tg_id(
        message.from_user.id
    )

    for i in await crud.get_list_groupslearns():
        
        try:
            if i.id_grouplearn == user_in_group_learn.id_grouplearn:
                text += f"<b>{i.id_grouplearn} | {i.title} | [*]</b>\n"
                continue
        except AttributeError:
            ...

        text += f"<b>{i.id_grouplearn} | {i.title}</b>\n"

    await message.answer(text)


@router_user_command.message(Command('groupsjoin'))
async def cmd_groups_join(message: Message, command: CommandObject):
    await user_is_reg_or_err(message)
    try:
        id_group_learn:int = int(command.args.split()[0])

    except ValueError:
        await message.answer("/groupsjoin <b>[id groups learns] id must be int</b>")

    data={
            "tg_id_student":message.from_user.id,
            "id_grouplearn":id_group_learn
    }

    await crud.join_groups_learn(
        data=schames.DS_GroupsSchames.model_validate_json(json.dumps(data))
    )

    await message.answer("Вы успешно вступили в группу")


@router_user_command.message(Command('groupscreate'))
async def cmd_groups_create(message: Message, command: CommandObject):
    await user_is_reg_or_err(message)
    data = {
        "tg_id_user": message.from_user.id,
        "title": command.args
    }

    await crud.create_groups_learns(
        schames.DS_GroupLearnsSchames.model_validate_json(json.dumps(data))
    )

    await message.answer(f"Вы успешно создали группу с названием:\n<b>{data['title']}</b>")
