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
    client = relationship("Client", back_populates="appointments", lazy="joined")
    professional_id = Column(Integer, ForeignKey("professionals.id"))
    professional = relationship(
        "Professional", back_populates="appointments", lazy="joined"
    )
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    schedule = relationship("Schedule", back_populates="appointments", lazy="joined")
    service_id = Column(Integer, ForeignKey("services.id"))
    service = relationship("Service", back_populates="appointments", lazy="joined")
