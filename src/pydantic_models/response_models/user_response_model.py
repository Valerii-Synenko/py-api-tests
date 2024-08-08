from datetime import datetime

from pydantic import BaseModel, field_validator


class CreateUserResponseModel(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

    @field_validator("createdAt")
    def validate_created_at(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            raise ValueError('"createdAt" must be in the format YYYY-MM-DDTHH:MM:SS.ffffffZ')
        return value


class RegisterUserResponseModel(BaseModel):
    id: int
    token: str
