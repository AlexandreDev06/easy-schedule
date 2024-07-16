import asyncio
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app import exceptions as exe
from app.configs import BaseCrud
from app.exceptions.internal_server_error_exception import exceptions_middleware
from app.helpers.get_current_username_swagger import get_current_username
from app.models.users import User
from app.routes import routers
from app.schemas import response_model
from app.services.auth_services import get_password_hash


@asynccontextmanager
async def create_admin_user(app: FastAPI):
    """Create admin user"""
    if not await BaseCrud(User).get_record(
        filters=[User.email == "admin@admin.com"], unique=True
    ):
        await BaseCrud(User).create_record(
            {
                "email": "admin@admin.com",
                "name": "Admin User",
                "password_digest": await get_password_hash("admin"),
            }
        )
    yield


app = FastAPI(
    responses=response_model,
    redoc_url=None,
    docs_url=None,
    openapi_url=None,
    lifespan=create_admin_user,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def get_documentation(_: str = Depends(get_current_username)):
    """Get swagger docs"""
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(_: str = Depends(get_current_username)):
    """Get openapi docs"""
    return get_openapi(title="demo-gpt", version="0.10.0", routes=app.routes)


# Exception handler 500
app.middleware("http")(exceptions_middleware)

# Handle data model error
app.exception_handler(RequestValidationError)(exe.validation_exception_handler)
app.exception_handler(exe.ValueNotFound)(exe.value_not_found)
app.exception_handler(exe.CredentialsException)(exe.credentials_invalid_exception)

app.include_router(routers)
