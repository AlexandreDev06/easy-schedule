from datetime import datetime
from typing import List, Optional

from app.configs.base import ApiBaseModel
from app.schemas.professional_schemas import ProfessionalSchema


class UserSchema(ApiBaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
