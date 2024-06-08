import secrets
import string
from datetime import UTC, datetime, timedelta

from fastapi import status
from jose import jwt
from passlib.context import CryptContext

from app.configs.base_crud import BaseCrud
from app.configs.settings import settings
from app.exceptions.internal_server_error_exception import get_http_exception
from app.models.users import User
from app.schemas.user_schemas import UserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password: str):
    return pwd_context.hash(password)


async def authenticate_user(email: str, password: str) -> User:
    email = email.strip().lower()
    user = await BaseCrud(User).get_record(filters=[User.email == email], unique=True)

    if not user or not await verify_password(password, user.password_digest):
        raise await get_http_exception("Email e/(ou) senha incorreto(s).", status.HTTP_401_UNAUTHORIZED)

    return user


async def create_access_token(
    payload: UserSchema,
    expires_in_minutes: int = int(settings.access_token_expires_in_minutes),
) -> str:
    to_encode = payload.model_dump()
    to_encode["created_at"] = to_encode["created_at"].isoformat()
    to_encode["updated_at"] = to_encode["updated_at"].isoformat()

    if expires_in_minutes:
        expire = datetime.now(tz=UTC) + timedelta(minutes=expires_in_minutes)
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt


async def user_exists(email: str) -> User:
    user = await BaseCrud(User).get_record(filters=[User.email == email], unique=True)
    if not user:
        raise await get_http_exception("Conta não encontrada.", status.HTTP_401_UNAUTHORIZED)

    return user


async def set_new_password(user: User, password: str = None):
    if password:
        new_password = password
    else:
        new_password = await generate_random_password()

    hashed_password = await get_password_hash(new_password)

    await BaseCrud(User).update_record(user.id, {"password_digest": hashed_password})

    return new_password


async def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
