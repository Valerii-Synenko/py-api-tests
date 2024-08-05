from src.pydantic_models.request_models.user_request_model import CreateUserRequestModel
from src.pydantic_models.response_models.user_response_model import CreateUserResponseModel, RegisterUserResponseModel
from src.response.response import AssertableResponse

from src.services.common_service import ComonServices


class UserApiServices(ComonServices):

    def register_new_user(self, user_email: str, user_password: str) -> AssertableResponse:
        """
        Method make registration of a new user.
        It makes the POST method to the "/register" endpoint, with the specific data
        :param user_email: The email with which will be registered a user
        :param user_password: The password with which the user will be registered
        :return: Response object (from Requests package)
        """
        user_payload = {"email": user_email, "password": user_password}
        response = self.perform_post_requests(endpoint="/register", payload=user_payload)
        return AssertableResponse(response=response)

    def create_new_user(self, user_name: str, user_job: str) -> tuple[int, CreateUserResponseModel]:
        """
        Method makes creation/addition of a new user.
        It makes the POST method to the "/user" endpoint, with the specific data
        :param user_name: The name with which will be created a user
        :param user_job: The user's job with which the user will be created
        :return: Tuple of two elements, CreateUserResponse pydantic model and response status code.
        """
        create_user_request_model = CreateUserRequestModel(name=user_name, job=user_job)
        response = self.perform_post_requests(endpoint="/users", payload=create_user_request_model.model_dump())
        create_user_response_model = CreateUserResponseModel(**response.json())

        return response.status_code, create_user_response_model
