from fastapi import APIRouter

from app.configs import BaseCrud
from app.models.users import User
from app.services.auth_services import get_password_hash

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
