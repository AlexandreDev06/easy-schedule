from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel
from app.schemas.professional_schemas import ProfessionalSchema
from app.schemas.service_schemas import ServiceSchema


class ScheduleSchema(ApiBaseModel):
    id: int
    start_at: datetime
    finish_at: datetime
    is_active: bool
    created_at: datetime
    updated_at: datetime

    professional_id: Optional[int] = None
    professional: Optional[ProfessionalSchema] = None
    service_id: Optional[int] = None
    service: Optional[ServiceSchema] = None


class PaginatedSchedulesSchema(ApiBaseModel):
    data: list[Optional[ScheduleSchema]]
    current_page: int
    total_pages: int
    total_records: int
