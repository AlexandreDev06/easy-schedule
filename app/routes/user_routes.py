from fastapi.routing import APIRouter

import app.controllers.users.users_controller as users_controller

user_router = APIRouter(tags=["Users"], prefix="/users")

user_router.put("/{user_id}")(users_controller.update)
user_router.get("/{user_id}")(users_controller.get_by_id)
