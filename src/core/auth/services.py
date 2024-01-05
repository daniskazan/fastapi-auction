from core.users.repositories import UserRepository
from core.users.domain import User
from core.common.utils.security import pwd_context


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
        self.__check_password(user=user, raw_password=raw_password)

    def __check_password(self, *, user: User, raw_password: str):
        if not pwd_context.verify(secret=raw_password, hash=user.password):
            raise