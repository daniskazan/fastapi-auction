from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from api.v1.users.dependencies import get_user_service
from api.v1.users.serializers import UserResponseSerializer
from core.common.utils.generic_response import OkResponse
from core.users.services import UserService
from core.users.exceptions import UserNotFoundError, UserNotFoundHTTPException


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}")
def get_user_by_id(
        user_id: UUID,
        user_service: UserService = Depends(get_user_service)
):
    try:
        user = user_service.find_user(user_id=user_id)
    except UserNotFoundError:
        raise UserNotFoundHTTPException
    return OkResponse.new(
        status_code=status.HTTP_200_OK, data=UserResponseSerializer.model_validate(user)
    )