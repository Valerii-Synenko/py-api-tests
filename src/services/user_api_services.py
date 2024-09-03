from http.client import responses

from src.pydantic_models.request_models.user_request_model import (
    CreateUserRequestModel,
    RegisterUserRequestModel,
)
from src.pydantic_models.response_models.get_user_respons_model import GetUserResponseModel
from src.pydantic_models.response_models.user_response_model import (
    CreateUserResponseModel,
    RegisterUserResponseModel,
)

from src.services.common_service import ComonServices


class UserApiServices(ComonServices):

    def register_new_user(self, email: str, password: str) -> tuple[int, RegisterUserResponseModel]:
        """
        Method make registration of a new user.
        It makes the POST method to the "/register" endpoint, with the specific data
        :param email: The email with which will be registered a user
        :param password: The password with which the user will be registered
        :return: Response status code and RegisterUserResponseModel
        """
        register_user_request_model = RegisterUserRequestModel(email=email, password=password)
        response = self._post(endpoint="/register", payload=register_user_request_model.model_dump())
        register_user_response_model = RegisterUserResponseModel(**response.json())

        return response.status_code, register_user_response_model

    def create_new_user(self, name: str, job: str) -> tuple[int, CreateUserResponseModel]:
        """
        Method makes creation/addition of a new user.
        It makes the POST method to the "/user" endpoint, with the specific data
        :param name: The name with which will be created a user
        :param job: The user's job with which the user will be created
        :return: Tuple of two elements, CreateUserResponse pydantic model and response status code.
        """
        create_user_request_model = CreateUserRequestModel(name=name, job=job)
        response = self._post(endpoint="/users", payload=create_user_request_model.model_dump())
        create_user_response_model = CreateUserResponseModel(**response.json())

        return response.status_code, create_user_response_model

    def get_user_by_id(self, user_id: str) -> tuple[int, GetUserResponseModel]:
        """
        Gets specified user by its id.
        Method makes GET request to /users/ endpoint.
        :param user_id: The id of expected user
        :return: Tuple with a response code and GetUserResponseModel object
        """
        response = self._get(endpoint=f"/users/{user_id}")

        responses_get_user_model = GetUserResponseModel(**response.json())

        return response.status_code, responses_get_user_model
