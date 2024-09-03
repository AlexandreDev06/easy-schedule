from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """Base class for all models"""

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class ApiBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
