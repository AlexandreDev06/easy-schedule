from fastapi.routing import APIRouter

import app.controllers.clients.clients_controller as clients_controller

client_router = APIRouter(tags=["Clients"], prefix="/clients")

client_router.get("/")(clients_controller.get_all)
