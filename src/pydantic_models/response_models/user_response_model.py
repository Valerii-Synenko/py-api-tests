from datetime import datetime

from pydantic import BaseModel, field_validator


class CreateUserResponseModel(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

    @field_validator("name")
    def check_name(cls, value):
        if len(value) < 0:
            raise ValueError('"name" must be a string with at least 1 length')
        return value

    @field_validator("job")
    def check_name(cls, value):
        if len(value) < 0:
            raise ValueError('"job" must be a string with at least 1 length')
        return value

    @field_validator("id")
    def check_name(cls, value):
        if len(value) < 0:
            raise ValueError('"id" must be a string with at least 1 length')
        return value

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
