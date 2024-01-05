from pydantic import BaseModel
from pydantic import ConfigDict


class PydanticBaseResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
