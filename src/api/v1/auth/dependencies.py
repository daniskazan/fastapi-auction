from core.common.session import Session
from core.users.repositories import UserRepository
from core.auth.services import AuthService


def get_auth_service() -> AuthService:
    return AuthService(user_repository=UserRepository(session=Session))
