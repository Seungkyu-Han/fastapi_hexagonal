import datetime

from pydantic import BaseModel, Field


class UserEntity(BaseModel):
    user_id: int
    name: str
    email: str
    encrypted_password: str
    created_at: datetime = Field(default=datetime.datetime.now())
