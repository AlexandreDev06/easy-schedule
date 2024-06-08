from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class UserSchema(ApiBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool
    prompt: Optional[str] = None
    session_token: Optional[str] = None
