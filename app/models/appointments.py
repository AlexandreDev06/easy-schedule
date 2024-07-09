from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Appointment(Base):
    """Appointment model that will be the time that client will be with the professional."""
    __tablename__ = "appointments"

    start_at = Column(DateTime, nullable=False)
    finish_at = Column(DateTime, nullable=False)
    notes = Column(String, nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="appointment")
    professional_id = Column(Integer, ForeignKey("professionals.id"))
    professional = relationship("Professional", back_populates="appointment")
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    schedule = relationship("Schedules", back_populates="schedule")
    service_id = Column(Integer, ForeignKey("services.id"))
    service = relationship("Service", back_populates="schedule")