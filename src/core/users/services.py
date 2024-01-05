from uuid import UUID

from core.users.domain import User
from core.users.repositories import UserRepository


class UserService:
    def __init__(self, *, repository: UserRepository) -> None:
        self.repository = repository

    def find_by_username(self, *, username: str) -> User:
        return self.repository.get_by_username(username=username)

    def find_user(self, *, user_id: UUID) -> User:
        return self.repository.get_by_id(user_id=user_id)
