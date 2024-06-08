from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

import app.services.auth_services as auth_services
from app.schemas.auth_schemas import OutputLoginSchema
from app.schemas.user_schemas import UserSchema


async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> OutputLoginSchema:
    """Authenticate user and return JWT token"""
    user = await auth_services.user_exists(form_data.username)

    await auth_services.authenticate_user(form_data.username, form_data.password)
    user_schema = UserSchema.model_validate(user)
    access_token = await auth_services.create_access_token(user_schema)

    return OutputLoginSchema(
        access_token=access_token,
        user=user_schema,
    )
