from fastapi import APIRouter

from .auth_routes import auth_router
from .health import router as router_health
from .session_routes import session_router
from .user_routes import user_router
from .webhook_routes import webhook_router

routers = APIRouter(prefix="/api/v1")

routers.include_router(auth_router)
routers.include_router(webhook_router)
routers.include_router(session_router)
routers.include_router(user_router)

routers.include_router(router_health)
