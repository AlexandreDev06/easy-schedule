from fastapi import Depends, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.configs.base_crud import BaseCrud
from app.configs.settings import settings
from app.exceptions.internal_server_error_exception import get_http_exception
from app.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


async def get_current_user(
    request: Request,
    token: str = Depends(oauth2_scheme),
) -> User:
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.jwt_algorithm]
        )
    except JWTError:
        raise await get_http_exception(
            "Email e/(ou) senha incorreto(s).", status.HTTP_401_UNAUTHORIZED
        )

    email: str = payload.get("email")

    current_user = await BaseCrud(User).get_record(
        filters=[User.email == email],
        unique=True,
    )

    if not current_user:
        raise await get_http_exception(
            "Usuário não autenticado.", status.HTTP_401_UNAUTHORIZED
        )

    # adds current_user to request state, so we can do things to user in application middleware
    request.state.current_user = current_user

    return current_user
