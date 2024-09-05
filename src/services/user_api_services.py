from src.pydantic_models.request_models.create_user_request_model import CreateUserRequestModel
from src.pydantic_models.request_models.update_user_request_model import UpdateUserRequest
from src.pydantic_models.request_models.register_user_request_model import RegisterUserRequestModel
from src.pydantic_models.response_models.create_user_response_model import CreateUserResponseModel
from src.pydantic_models.response_models.get_user_respons_model import GetUserResponseModel
from src.pydantic_models.response_models.get_users_respons_vodel import GetListOfUsersResponseModel
from src.pydantic_models.response_models.register_user_response_model import RegisterUserResponseModel
from src.pydantic_models.response_models.update_user_response_model import UpdateUseResponse

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

    def get_list_of_users(self, page_number: int) -> tuple[int, GetListOfUsersResponseModel]:
        """
        Gets a list of user per specific page.
        Method makes GET request to /users/ endpoint with specified parameters
        :param page_number: Page from which will be getting the list.
        :return: Tuple with status code and GetListOfUsersResponseModel object
        """

        response = self._get(endpoint=f"/users", params={"page": page_number})

        response_model = GetListOfUsersResponseModel(**response.json())

        return response.status_code, response_model


    def update_user_by_patch_method(self, user_id: int, user_model: UpdateUserRequest) -> tuple[int, UpdateUseResponse]:
        """
        Updates a user resource using the PATCH method.

        This method sends a PATCH request to update the user information with the specified user ID.
        The request payload is constructed from the provided `user_model`, and the response is parsed
        into an `UpdateUseResponse` object.

        :param user_id: The ID of the user to be updated.
        :param user_model: The data to be used for updating the user. Fields can be optional.
        :return: tuple with int and an oject of the UpdateUseResponse model
        """
        response = self._patch(endpoint=f"/users/{user_id}", payload=user_model.model_dump())
        response_body_as_pydantic_model = UpdateUseResponse(**response.json())
        return response.status_code, response_body_as_pydantic_model
