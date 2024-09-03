from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel
from app.schemas.client_schemas import ClientSchema
from app.schemas.professional_schemas import ProfessionalSchema
from app.schemas.schedule_schemas import ScheduleSchema
from app.schemas.service_schemas import ServiceSchema


class AppointmentSchema(ApiBaseModel):
    id: int
    start_at: datetime
    finish_at: datetime
    notes: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    client_id: Optional[int] = None
    client: Optional[ClientSchema] = None
    professional_id: Optional[int] = None
    professional: Optional[ProfessionalSchema]
    schedule_id: Optional[int] = None
    schedule: Optional[ScheduleSchema] = None
    service_id: Optional[int] = None
    service: Optional[ServiceSchema] = None

class PostAppointmentSchema(ApiBaseModel):
    start_at: Optional[datetime] = None
    finish_at: Optional[datetime] = None
    notes: Optional[str] = None
    client_id: Optional[int] = None
    professional_id: Optional[int] = None
    schedule_id: Optional[int] = None
    service_id: Optional[int] = None

class PaginatedAppointmentsSchema(ApiBaseModel):
    data: list[Optional[AppointmentSchema]]
    current_page: int
    total_pages: int
    total_records: int
