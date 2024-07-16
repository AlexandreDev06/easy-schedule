from datetime import datetime

from app.configs.base import ApiBaseModel


class UserSchema(ApiBaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
