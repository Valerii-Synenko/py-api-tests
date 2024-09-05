from pydantic import BaseModel


class CreateUserRequestModel(BaseModel):
    """
    A moder represent the request for a new user creation.
    Attributes:
        name (str): The name for a new user.
        job (str): The job title for the new user.
    """

    name: str
    job: str

    def __repr__(self):
        """
        Return a string representation of the CreateUserRequestModel instance.
        The string includes the class name and the values of the 'name' and 'job' attributes.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, job={self.job!r})"