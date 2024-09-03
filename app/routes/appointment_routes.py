from fastapi.routing import APIRouter

import app.controllers.appointments.appointments_controller as appointments_controller

appointment_router = APIRouter(tags=["Appointments"], prefix="/appointments")

appointment_router.get("/")(appointments_controller.get_all)
appointment_router.post("/")(appointments_controller.create)