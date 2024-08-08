from pydantic import BaseModel, field_validator


class CreateUserRequestModel(BaseModel):
    name: str
    job: str


class RegisterUserRequestModel(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def validate_email(cls, value):
        specified_emails = [
            "george.bluth@reqres.in",
            "janet.weaver@reqres.in",
            "emma.wong@reqres.in",
            "eve.holt@reqres.in",
            "charles.morris@reqres.in",
            "tracey.ramos@reqres.in",
        ]

        if value not in specified_emails:
            raise ValueError(f"'email' must be one of the member of the {specified_emails}")
        return value
