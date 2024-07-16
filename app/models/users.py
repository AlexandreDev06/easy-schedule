from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class User(Base):
    """User model to login"""

    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password_digest = Column(String, nullable=True)
    name = Column(String, nullable=True)

    professionals = relationship("Professional", back_populates="user")
    clients = relationship("Client", back_populates="user")
