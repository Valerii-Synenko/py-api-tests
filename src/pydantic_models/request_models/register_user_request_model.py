from pydantic import BaseModel, field_validator


# class CreateUserRequestModel(BaseModel):
#     """
#     A moder represent the request for a new user creation.
#     Attributes:
#         name (str): The name for a new user.
#         job (str): The job title for the new user.
#     """
#
#     name: str
#     job: str
#
#     def __repr__(self):
#         """
#         Return a string representation of the CreateUserRequestModel instance.
#         The string includes the class name and the values of the 'name' and 'job' attributes.
#         """
#         return f"{self.__class__.__name__}(name={self.name!r}, job={self.job!r})"


class RegisterUserRequestModel(BaseModel):
    """
    A moder represent the request for a new user registration.
    Attributes:
        email (str): One of the five accepted emails.
        password (str): A password for the user.
    """

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

    def __repr__(self):
        """
        Return a string representation of the RegisterUserRequestModel instance.
        The string includes the class name and the values of the 'email' and 'password' attributes.
        """
        return f"{self.__class__.__name__}(email={self.email!r}, password={self.password!r})"
