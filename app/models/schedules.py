from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Schedules(Base):
    """Schedule model that will be the time that professional will be available."""
    __tablename__ = "schedules"

    start_at = Column(DateTime, nullable=False)
    finish_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    professional_id = Column(Integer, ForeignKey("professionals.id"))
    professional = relationship("Professional", back_populates="schedule")
    service_id = Column(Integer, ForeignKey("services.id"))
    service = relationship("Service", back_populates="schedule")
    appointments = relationship("Appointment", back_populates="schedule")
