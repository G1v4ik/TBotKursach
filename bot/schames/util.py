from httpx import Response
from .schames import BaseModel
from json import dumps

from pydantic import ValidationError

def response_to_schames(
    response: Response, 
    schames: BaseModel
) -> BaseModel:
    try:
        return schames.model_validate_json(dumps(response.json()))
    except ValidationError:
        return None

def response_to_list_schames(
    response: Response, 
    schames: BaseModel
) -> list[BaseModel]:
    
    data = response.json()
    try:
        return [schames.model_validate_json(dumps(i)) for i in data]
    except ValidationError:
        return None