from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Professional(Base):
    """Professional model to login and to show the schedule."""
    __tablename__ = "professionals"

    email = Column(String, nullable=False, unique=True)
    password_digest = Column(String, nullable=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="professional")
