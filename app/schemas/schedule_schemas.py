from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class ScheduleSchema(ApiBaseModel):
    id: int
    start_at: datetime
    finish_at: datetime
    is_active: bool
    created_at: datetime
    updated_at: datetime

    professional_id: Optional[int] = None
    service_id = Optional[int] = None
