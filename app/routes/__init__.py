from fastapi import APIRouter

from .auth_routes import auth_router
from .health import router as router_health

routers = APIRouter(prefix="/api/v1")

routers.include_router(auth_router)

routers.include_router(router_health)
