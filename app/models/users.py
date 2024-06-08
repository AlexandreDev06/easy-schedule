from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class User(Base):
    """User model to login"""

    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password_digest = Column(String, nullable=True)
    session_token = Column(String, nullable=True)
    prompt = Column(String, nullable=True)
    name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    messages = relationship("Message", back_populates="user", lazy="joined")
