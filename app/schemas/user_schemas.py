from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


# NEED REFACTOR
# NAO TEM NECESSIDADE UTILIZAR ESSAS CLASSES A MAIS SO PRA RETORNAR RELACAO, DPS TENTA REMOVER ELAS E JUNTAR EM UM LUGAR SO
class ServiceWithoutRelationshipsSchema(ApiBaseModel):
    id: int
    name: str
    price: int
    duration: int
    description: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class ProfessionalWithoutRelationshipsSchema(ApiBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool
    prompt: Optional[str] = None
    session_token: Optional[str] = None
    user_id: Optional[int] = None
    services: Optional[list[ServiceWithoutRelationshipsSchema]] = []


class UserSchema(ApiBaseModel):
    id: int
    email: str
    name: Optional[str]
    created_at: datetime
    updated_at: datetime
    professionals: Optional[list[ProfessionalWithoutRelationshipsSchema]]
