from datetime import datetime

from pydantic import field_validator, BaseModel


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

    def __repr__(self):
        """
        Return a string representation of the CreateUserResponseModel instance.
        The string includes the class name and the values of the 'name', 'job', 'id and 'createdAt' attributes.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, job={self.job!r}, id={self.id!r}, createdAt={self.createdAt!r})"
