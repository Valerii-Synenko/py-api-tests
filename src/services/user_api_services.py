import requests

from src.services.common_service import ComonServices


class UserApiServices(ComonServices):

    def register_new_user(self, user_email: str, user_password: str) -> requests.Response:
        """
        Method make registration of a new user.
        It makes the POST method to the "/register" endpoint, with the specific data
        :param user_email: The email with which will be registered a user
        :param user_password: The password with which the user will be registered
        :return: Response object (from Requests package)
        """
        user_payload = {"email": user_email, "password": user_password}
        return self.perform_post_requests(endpoint="/register", payload=user_payload)

    def create_new_user(self, user_name: str, user_jod: str) -> requests.Response:
        """
        Method makes creation/addition of a new user.
        It makes the POST method to the "/register" endpoint, with the specific data
        :param user_name: The name with which will be created a user
        :param user_jod: The user's job with which the user will be created
        :return: Response object (from Requests package)
        """
        user_payload = {"name": user_name, "job": user_jod}
        return self.perform_post_requests(endpoint="/users", payload=user_payload)