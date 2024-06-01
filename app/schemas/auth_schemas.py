from typing import List, Optional

from pydantic import BaseModel

from app.schemas.user_schemas import UserSchema


class OutputLoginSchema(BaseModel):
    access_token: Optional[str] = None
    user: UserSchema


class FirstAccessInputSchema(BaseModel):
    username: str
    password: str


class ForgotPasswordInputSchema(BaseModel):
    username: str
