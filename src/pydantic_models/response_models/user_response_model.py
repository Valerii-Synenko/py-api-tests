from datetime import datetime

from pydantic import BaseModel, field_validator


class CreateUserResponseModel(BaseModel):
    """
    A model representing the response received after creating a user.

    Attributes:
        name (str): The name of the created user.
        job (str): The job title of the created user.
        id (str): The unique identifier assigned to the user.
        createdAt (str): The timestamp when the user was created, expected to be in ISO 8601 format.
    """
    name: str
    job: str
    id: str
    createdAt: str

    @field_validator("createdAt")
    def validate_created_at(cls, value) -> str:
        """
        Validates that the 'createdAt' field in the user creation response is in the ISO 8601 format.

        :param value: The timestamp string to be validated.
        :return: The validated timestamp string.
        :raises ValueError: If the timestamp is not in the expected ISO 8601 format (YYYY-MM-DDTHH:MM:SS.ffffffZ).
        """
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            raise ValueError("'createdAt' must be in the format YYYY-MM-DDTHH:MM:SS.ffffffZ")
        return value


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
