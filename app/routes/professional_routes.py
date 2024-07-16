from fastapi.routing import APIRouter

import app.controllers.professionals.professionals_controller as professionals_controller

professional_router = APIRouter(tags=["Professionals"], prefix="/professionals")

professional_router.get("/")(professionals_controller.get_all)
