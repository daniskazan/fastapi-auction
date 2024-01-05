from uuid import UUID

from core.common.serializers.base import PydanticBaseResponseModel


class UserResponseSerializer(PydanticBaseResponseModel):
    user_id: UUID
    username: str
    email: str
