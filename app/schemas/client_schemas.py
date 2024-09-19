from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class ClientSchema(ApiBaseModel):
    id: int
    name: str
    cpf: str
    email: str
    created_at: datetime
    updated_at: datetime

    user_id: Optional[int] = None


class PaginatedClientsSchema(ApiBaseModel):
    data: list[Optional[ClientSchema]]
    current_page: int
    total_pages: int
    total_records: int


class PostClientSchema(ApiBaseModel):
    name: str
    cpf: str
    email: str
    cell_phone: str
    user_id: Optional[int] = None