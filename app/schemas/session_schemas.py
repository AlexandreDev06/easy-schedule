from datetime import datetime
from typing import Optional

from app.configs.base import ApiBaseModel


class StatusSessionResponseSchema(ApiBaseModel):
    id: str
