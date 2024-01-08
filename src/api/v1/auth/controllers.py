from uuid import UUID
import datetime as dt

import jose.exceptions
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError

from api.v1.auth.dependencies import get_auth_service
from api.v1.users.dependencies import get_user_service
from api.v1.auth.serializers import (
    RegistrationBodyRequest,
    RegistrationResponseSerializer,
    LoginBody,
)
from config import app_config
from core.users.services import UserService
from core.auth.services import AuthService
from core.users.exceptions import (
    UserAlreadyExistsError,
    UserAlreadyExistsHTTPException,
    UserNotFoundError,
    UserNotFoundHTTPException,
)
from core.auth.exceptions import (
    InvalidCredentialsError,
    InvalidCredentialsHTTPException,
    TokenExpiredHTTPException,
    BadTokenHTTPException,
)
from core.users.domain import User
from core.common.utils.generic_response import OkResponse

router = APIRouter(prefix="/auth", tags=["auth"])
security = HTTPBearer()


def get_request_user_or_401(
    *, token: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    try:
        payload = jwt.decode(
                token.credentials,
                app_config.JWT_SECRET_KEY,
                algorithms=app_config.JWT_ALGORITHM,
            )
        user_id: UUID = payload.get("sub")
        username: str = payload.get("username")
        email: str = payload.get("email")
    except ExpiredSignatureError:
        raise TokenExpiredHTTPException
    return User(user_id=user_id, username=username, email=email, password="<secret>")


@router.post("/register", response_model=OkResponse[RegistrationResponseSerializer])
def register(
    body: RegistrationBodyRequest, auth_service: AuthService = Depends(get_auth_service)
):
    try:
        user = User(username=body.username, password=body.password, email=body.email)
        new_user: User = auth_service.register(user=user)
    except UserAlreadyExistsError:
        raise UserAlreadyExistsHTTPException
    return OkResponse.new(
        status_code=status.HTTP_201_CREATED,
        data=RegistrationResponseSerializer.model_validate(new_user),
    )


@router.post(
    "/login",
)
def login(
    body: LoginBody = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
    user_service: UserService = Depends(get_user_service),
):
    try:
        user: User = user_service.find_by_username(username=body.username)
        token: str = auth_service.login(user=user, raw_password=body.password)
    except (UserNotFoundError, InvalidCredentialsError):
        raise InvalidCredentialsHTTPException
    return OkResponse.new(status_code=status.HTTP_200_OK, data=token)


@router.get("/ddd")
def ddd(user: User = Depends(get_request_user_or_401)):
    return 1
