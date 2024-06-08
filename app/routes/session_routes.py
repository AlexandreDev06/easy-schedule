from fastapi.routing import APIRouter

import app.controllers.sessions.sessions_controller as sessions_controller

session_router = APIRouter(tags=["Sessions Management"])

session_router.post("/start-session")(sessions_controller.connect_qrcode)
session_router.get("/status-session")(sessions_controller.status_session)
session_router.post("/close-session")(sessions_controller.close_session)
