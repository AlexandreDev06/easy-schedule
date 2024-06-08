

from app.configs.base_crud import BaseCrud
from app.models.users import User
from app.schemas.user_schemas import UserSchema


async def update(user_id: int, data: UserSchema) -> UserSchema:
    """Update user by id"""
    await BaseCrud(User).update_record(user_id, data)
    user = await BaseCrud(User).get_record(instance_id=user_id)
    return UserSchema(**user.__dict__)

async def get_by_id(user_id: int) -> UserSchema:
    """Get user by id"""
    user = await BaseCrud(User).get_record(filters=[User.id == user_id], unique=True)
    return UserSchema(**user.__dict__)