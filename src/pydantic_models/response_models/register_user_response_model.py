from pydantic import BaseModel, field_validator


class RegisterUserResponseModel(BaseModel):
    """
    A model representing the response received after registering a user.

    Attributes:
        id (int): The unique identifier assigned to the user.
        token (str): The authentication token assigned to the user, expected to be 17 characters long.
    """

    id: int
    token: str

    @field_validator("token")
    def validate_token(cls, value) -> str:
        """
        Validates that the 'token' field contains exactly 17 characters.

        :param value: The token string to be validated.
        :return: The validated token string.
        :raises ValueError: If the token does not contain exactly 17 characters.
        """
        if not len(value) == 17:
            raise ValueError(f"Expected 'token' length is 17, but received {len(value)} characters.")
        return value

    def __repr__(self):
        """
        Return a string representation of the RegisterUserResponseModel instance.
        The string includes the class name and the values of the 'id' and 'token' attributes.
        """
        return f"{self.__class__.__name__}\n id={self.id!r}\n token={self.token!r}"
