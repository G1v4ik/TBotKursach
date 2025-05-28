from .pressf import Client
from bot.schames import schames, util

from pydantic_core import ValidationError

import json


async def is_user_reg(
        telegram_id: int
    ) -> schames.DS_TG_ID_Schames:

    have_user = await Client.get(
        schames_output=schames.DS_TG_ID_Schames,
        endpoint='/users/',
        id_object=telegram_id
    )
    try:
        schames.DS_TG_ID_Schames.model_validate_json(
            json.dumps(have_user.json())
        )
        return True
    except ValidationError:
        return False
    
    except json.decoder.JSONDecodeError:
        return False


async def get_user_by_tg_id_or_None(
        telegram_id
    ) -> schames.DS_UserSchames | None:
    try:
        get_user = await Client.get(
            schames_output=schames.DS_UserSchames,
            endpoint='/users/',
            id_object=telegram_id
        )
        if get_user.json() is not None:
            return util.response_to_schames(
                get_user, 
                schames.DS_UserSchames
            )
    except json.decoder.JSONDecodeError:
        return None


async def get_list_user() -> list[schames.DS_UserSchames]:
    get_list = await Client.list(
        schames_output=schames.DS_UserSchames,
        endpoint='/users'
    )
    return [schames.DS_UserSchames.model_validate_json(json.dumps(i)) for i in get_list]


async def registration_user(
        data: schames.DS_UserSchames
    ) -> schames.DS_UserSchames:
    
    create_user = await Client.create(
        schames_input=data,
        endpoint='/users'
    )
    
    return util.response_to_schames(
        create_user, schames.DS_UserSchames
    )



#Groups learns

async def get_list_groupslearns(
) -> list[schames.DS_GroupLearnsListSchames]:
    
    get_groupslearns = await Client.list(
        schames_output=schames.DS_GroupLearnsListSchames,
        endpoint='/groups-learns'
    )

    return util.response_to_list_schames(
        get_groupslearns, schames.DS_GroupLearnsListSchames
    )


async def get_groups_by_tg_id(
    telegram_id: int
) -> schames.DS_GroupLearnsSchames:
    get_groups = await Client.get(
        schames_output=schames.DS_GroupLearnsSchames,
        endpoint='/groups/tg_id/',
        id_object=telegram_id
    )
    return util.response_to_schames(
        get_groups, schames.DS_GroupsSchames
    )


async def join_groups_learn(
        data: schames.DS_GroupsSchames
) -> schames.DS_GroupsSchames:
    join_grouops = await Client.create(
        schames_input=data,
        endpoint='/groups'
    )
    return util.response_to_schames(
        join_grouops, schames.DS_GroupsSchames
    )


async def create_groups_learns(
    data: schames.DS_GroupLearnsSchames
) -> schames.DS_GroupLearnsSchames:
    
    create_group = await Client.create(
        schames_input=data,
        endpoint='/groups-learns'
    )

    return util.response_to_schames(
        create_group, schames.DS_GroupLearnsSchames
    )