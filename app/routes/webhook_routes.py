from fastapi.routing import APIRouter

import app.controllers.webhook.webhook_controller as webhook_controller

webhook_router = APIRouter(tags=["Webhook"])

webhook_router.post("/answer/{session_token}")(webhook_controller.answer_message)
