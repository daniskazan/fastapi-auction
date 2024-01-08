import datetime as dt

from jose import jwt

from core.users.repositories import UserRepository
from core.users.domain import User
from core.common.utils.security import pwd_context
from core.auth.exceptions import InvalidCredentialsError
from config import app_config


class AuthService:
    def __init__(
            self,
            *,
            user_repository: UserRepository
    ):
        self.user_repository = user_repository

    def register(self, *, user: User) -> User:
        return self.user_repository.save(user=user)

    def login(self, *, user: User, raw_password: str):
        self.__verify_password(user=user, raw_password=raw_password)
        token = self.__create_access_token(user=user)
        return token

    @staticmethod
    def __verify_password(*, user: User, raw_password: str) -> None:
        if not pwd_context.verify(secret=raw_password, hash=user.password):
            raise InvalidCredentialsError

    @staticmethod
    def __create_access_token(*, user: User) -> str:
        claims = {
            "sub": str(user.user_id),
            "username": user.username,
            "email": user.email,
            "exp": dt.datetime.utcnow() + dt.timedelta(minutes=10)
        }
        token: str = jwt.encode(claims=claims, key=app_config.JWT_SECRET_KEY)
        print(jwt.decode(token=token, key=app_config.JWT_SECRET_KEY))
        return token
