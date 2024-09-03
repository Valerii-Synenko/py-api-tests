from pydantic import BaseModel

from src.pydantic_models.response_models.get_user_respons_model import Support, Data


class GetListOfUsersResponseModel(BaseModel):
    """
    A model representing the response from an API call to get a list of users.
    Attributes:
        page (int): The current page number.
        per_page (int): The number of users per page.
        total (int): The total number of users available.
        total_pages (int): The total number of pages available.
        data (list[Data]): A list of user data objects.
        support (Support): Support information associated with the request.
    """

    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[Data]
    support: Support

    def __repr__(self):
        """
        Provides a string representation of the GetListOfUsersResponseModel object,
        including all its attributes.

        :return: A formatted string that represents the object.
        """
        return (
            f"{self.__class__.__name__}\n"
            f"page={self.page!r}\n"
            f"per_page={self.per_page!r}\n"
            f"total={self.total!r}\n"
            f"total_pages={self.total_pages!r}\n"
            f"data={self.data!r}\n"
            f"support={self.support!r}\n"
        )
