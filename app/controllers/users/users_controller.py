from fastapi import Depends

from app.configs import BaseCrud
from app.helpers.get_current_user import get_current_user
from app.models.users import User
from app.schemas.user_schemas import UserSchema


async def update(
    user_id: int, data: UserSchema, current_user: str = Depends(get_current_user)
) -> UserSchema:
    """Update user by id"""
    await BaseCrud(User).update_record(user_id, data)
    user = await BaseCrud(User).get_record(instance_id=user_id)
    return UserSchema(**user.__dict__)


async def get_by_id(
    user_id: int, current_user: str = Depends(get_current_user)
) -> UserSchema:
    """Get user by id"""
    user = await BaseCrud(User).get_record(filters=[User.id == user_id], unique=True)
    return UserSchema(**user.__dict__)
