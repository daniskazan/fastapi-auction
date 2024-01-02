from typing import Generic, TypeAlias, TypeVar, Union, Tuple, Iterable

from pydantic import BaseModel
from pydantic import conint


T = TypeVar("T")


StatusCode: TypeAlias = int
AdditionalResponseSchema = TypeVar("AdditionalResponseSchema", bound=BaseModel)
Responses: TypeAlias = Union[
    Tuple[StatusCode, AdditionalResponseSchema],
    Iterable[Tuple[StatusCode, AdditionalResponseSchema]],
]
StatusCodeToResponseSchemaMapping: TypeAlias = dict


def additional_responses(responses: Responses) -> StatusCodeToResponseSchemaMapping:
    data = {}
    if isinstance(responses, tuple):
        code, schema = responses
        data.update({code: {"model": schema}})
        return data

    else:
        for code, schema in responses:
            data.update({code: {"model": schema}})
        return data


class OkResponse(BaseModel, Generic[T]):
    status_code: conint(ge=200, le=299)
    data: T

    @classmethod
    def new(cls, *, status_code: int, data: T):
        return cls(status_code=status_code, data=data)