from pydantic import BaseModel, Field

from typing import Optional, Annotated

from datetime import datetime


class DS_support_new_message(BaseModel):
    telegram_id: int
    username: str
    message: str

class DS_response_message(DS_support_new_message):
    id_message: int
    is_new: bool = False
    create_at: datetime