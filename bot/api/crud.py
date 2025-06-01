from .pressf import Client
from bot.schames import schames

from pydantic_core import ValidationError

import json


async def list_response_to_schames(
        _response, 
        _schames: schames.BaseModel
):
    return [_schames.model_validate_json(json.dumps(i)) for i in _response.json()]


async def send_support_message_from_user(
    data: schames.DS_support_new_message
):
    
    send_message = await Client.create(
        schames_input=data,
        endpoint='/support_messages'
    )
    return send_message
    


async def get_list_support_message():
    list_message = await Client.list(
        schames.DS_response_message,
        endpoint='/support_messages'
    )
    return await list_response_to_schames(
        list_message,
        schames.DS_response_message
    )
    

async def response_support_message(
        id_message: int
):
    send_message = await Client.patch(
        id_message,
        endpoint='/support_messages'
    )
    return send_message