from datetime import datetime, timezone
from uuid import uuid4
from pydantic import BaseModel, validator
from typing import Generic, TypeVar


T = TypeVar('T', bound=BaseModel)


class Request(BaseModel, Generic[T]):
    request_id: str
    request_time: str
    request_data: T


class Response(BaseModel, Generic[T]):
    response_id: str = ''
    response_time: str = ''
    response_data: T

    @validator('response_time', pre=True, always=True)
    def set_response_time(cls, v):
        return v or datetime.now(timezone.utc).astimezone().isoformat()

    @validator('response_id', pre=True, always=True)
    def set_response_id(cls, v):
        return v or uuid4().__str__()
