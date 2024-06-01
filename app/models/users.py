from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class User(Base):
    """User model to login"""

    __tablename__ = "users"

    email = Column(String, nullable=False)
    password_digest = Column(String, nullable=True)

    name = Column(String, nullable=True)
