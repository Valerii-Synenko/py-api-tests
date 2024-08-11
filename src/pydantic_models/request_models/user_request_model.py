from pydantic import BaseModel, field_validator


class CreateUserRequestModel(BaseModel):
    name: str
    job: str


class RegisterUserRequestModel(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def validate_email(cls, value) -> str:
        """
        Validates that only specific emails could be used for the registration.
        By the system design, we can register a user only with one of the predefined emails.
        :param value: The email that must be validated.
        :return: The str value of the validated email.
        """
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
