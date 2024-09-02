import re

from pydantic import BaseModel, field_validator


class Data(BaseModel):
    """Represents the user data returned in the API response."""

    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator("avatar")
    def validate_avatar_url(cls, value) -> str:
        """
        Validates the avatar URL to ensure it matches the expected format.
        :param value: The avatar URL to validate.

        :returns: The validated avatar URL.

        :raises ValueError: If the avatar URL does not match the expected pattern.
        """
        pattern = re.compile(r"https://reqres\.in/img/faces/\d+-image\.jpg")
        if not pattern.match(str(value)):
            raise ValueError("Invalid image URL format")
        return value


class Support(BaseModel):
    """Represents the support information provided in the API response."""

    url: str = "https://reqres.in/#support-heading"
    text: str = "To keep ReqRes free, contributions towards server costs are appreciated!"


class GetUserResponseModel(BaseModel):
    """Represents the full API response including user data and support information."""

    data: Data
    support: Support

    def __repr__(self):
        """
        Custom string representation of the GetUserResponseModel instance.
        :return: A string representation of the model including data and support information.
        """
        return f"{self.__class__.__name__} \n data: {self.data!r} \n support: {self.support!r}"
