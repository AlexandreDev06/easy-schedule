from fastapi.routing import APIRouter

import app.controllers.auth.auth_controller as auth_controller

auth_router = APIRouter(tags=["Auth"])

auth_router.post("/login")(auth_controller.login)
