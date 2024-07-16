from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Service(Base):
    """Service model that will be the service that professional will provide."""

    __tablename__ = "services"

    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    professional_id = Column(Integer, ForeignKey("professionals.id"))
    professional = relationship(
        "Professional", back_populates="services", lazy="joined"
    )
    appointments = relationship("Appointment", back_populates="service")
    schedules = relationship("Schedule", back_populates="service")
