from fastapi import APIRouter

from app.configs.base_crud import BaseCrud
from app.controllers.auth.services.auth_services import get_password_hash
from app.models.users import User

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_checker():
    """Health checker endpoint"""
    # Create a test user
    # await BaseCrud(User).create_record(
    #     {
    #         "email": "test@email.com",
    #         "name": "Test User",
    #         "password_digest": await get_password_hash("password"),
    #     }
    # )

    return {"success": True}
