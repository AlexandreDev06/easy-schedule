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
    schedule_id: Optional[int] = None
    service_id: Optional[int] = None
