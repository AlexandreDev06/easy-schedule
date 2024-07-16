from fastapi import APIRouter

from .appointment_routes import appointment_router
from .auth_routes import auth_router
from .client_routes import client_router
from .health import router as router_health
from .professional_routes import professional_router
from .schedule_routes import schedule_router
from .session_routes import session_router
from .user_routes import user_router
from .webhook_routes import webhook_router

routers = APIRouter(prefix="/api/v1")

routers.include_router(auth_router)
routers.include_router(webhook_router)
routers.include_router(session_router)
routers.include_router(user_router)
routers.include_router(appointment_router)
routers.include_router(client_router)
routers.include_router(professional_router)
routers.include_router(schedule_router)

routers.include_router(router_health)
