from uuid import UUID

from pydantic import Field
from pydantic import BaseModel
from pydantic import EmailStr
from core.common.serializers.base import PydanticBaseResponseModel


class RegistrationBodyRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


class RegistrationResponseSerializer(PydanticBaseResponseModel):
    user_id: UUID
    username: str
    email: str


class LoginBody(BaseModel):
    username: str = Field(description="Username or email")
    password: str


class LoginResponseSerializer(PydanticBaseResponseModel):
    "JWT Tokens"
    pass
