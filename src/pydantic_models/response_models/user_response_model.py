from pydantic import BaseModel


class CreateUserResponseModel(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class RegisterUserResponseModel(BaseModel):
    id: int
    token: str
