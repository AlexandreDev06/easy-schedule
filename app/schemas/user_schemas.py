from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class UserSchema(ApiBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
