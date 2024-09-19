from sqlalchemy import (
    ARRAY,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Time,
)
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Schedule(Base):
    """Schedule model that will be the time that professional will be available.
    essa vai ser a agenda do profissional, onde ele vai estar disponível para atendimento
    entao vai ter horario de inicio e final de atendimento
    quais dias da semana ele atende
    horario de comeco intervalo
    horario final de intervalor
    """

    __tablename__ = "schedules"

    start_at = Column(Time, nullable=False)
    finish_at = Column(Time, nullable=False)
    is_active = Column(Boolean, default=True)
    interval_start_at = Column(Time, nullable=True)
    interval_finish_at = Column(Time, nullable=True)
    weekdays = Column(ARRAY(Integer), nullable=False)

    professional_id = Column(Integer, ForeignKey("professionals.id"))
    professional = relationship(
        "Professional", back_populates="schedules"
    )
    service_id = Column(Integer, ForeignKey("services.id"))
    service = relationship("Service", back_populates="schedules")
    appointments = relationship("Appointment", back_populates="schedule")
