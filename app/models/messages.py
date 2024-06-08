from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.base import Base


class Message(Base):
    """Message model to save messages from user and gpt"""

    __tablename__ = "messages"

    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    content = Column(String, nullable=True)
    role = Column(String, nullable=True)  # can be system or user

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="messages")
