from pydantic import BaseModel, Field

from typing import Optional, Annotated



_surname = Annotated[str, Field(max_length=30)]
# _contact_phone = Annotated[str, Field(max_length=12)]

class DS_TG_ID_Schames(BaseModel):
    telegram_id: int

class DS_UserSchames(DS_TG_ID_Schames):
    name: str = Field(max_length=30)
    surname: Optional[_surname] = None
    contact_phone: Optional[str] = None
    user_type: Optional[str] = None


class DS_GroupLearnsSchames(BaseModel):
    tg_id_user: int
    title: str = Field(max_length=100)


class DS_GroupLearnsListSchames(DS_GroupLearnsSchames):
    id_grouplearn: int = None


class DS_GroupsSchames(BaseModel):
    tg_id_student: int
    id_grouplearn: int
