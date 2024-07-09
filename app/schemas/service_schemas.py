from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class ServiceSchema(ApiBaseModel):
    id: int
    name: str
    price: int
    duration: int
    description: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    professional_id: Optional[int] = None
