from fastapi.routing import APIRouter

import app.controllers.schedules.schedules_controller as schedules_controller

schedule_router = APIRouter(tags=["Schedules"], prefix="/schedules")

schedule_router.get("/")(schedules_controller.get_all)
schedule_router.post("/")(schedules_controller.create)
