from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    id: int
    email: str
    name: Optional[str]
    created_at: datetime
    updated_at: datetime


class OutputLoginSchema(BaseModel):
    access_token: Optional[str] = None
    user: UserLoginSchema


class FirstAccessInputSchema(BaseModel):
    username: str
    password: str


class ForgotPasswordInputSchema(BaseModel):
    username: str
