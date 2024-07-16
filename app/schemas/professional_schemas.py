from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel
from app.schemas.user_schemas import UserSchema


class ProfessionalSchema(ApiBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool
    prompt: Optional[str] = None
    session_token: Optional[str] = None

    user_id: Optional[int] = None
    user: Optional[UserSchema] = None


class PaginatedProfessionalsSchema(ApiBaseModel):
    data: list[Optional[ProfessionalSchema]]
    current_page: int
    total_pages: int
    total_records: int
