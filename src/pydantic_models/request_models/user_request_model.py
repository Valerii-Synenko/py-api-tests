from pydantic import BaseModel


class CreateUserRequestModel(BaseModel):
    name: str
    job: str


class RegisterUserRequestModel(BaseModel):
    email: str
    password: str
