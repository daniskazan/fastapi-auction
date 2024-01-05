from core.users.services import UserService
from core.users.repositories import UserRepository
from core.common.session import Session


def get_user_service() -> UserService:
    return UserService(repository=UserRepository(session=Session))
