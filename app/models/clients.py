from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Client(Base):
    """Client model to mark an appointment."""

    __tablename__ = "clients"

    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    cellphone = Column(String, nullable=True)
    # birthdate = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="clients")
    appointments = relationship(
        "Appointment", back_populates="client", cascade="all, delete"
    )
