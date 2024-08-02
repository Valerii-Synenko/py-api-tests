import json

import requests


class ComonServices:

    def __init__(self):
        self.base_url = "https://reqres.in/api"
        self.request_headers = {"Content-Type": "application/json"}

    def perform_post_requests(self, endpoint: str, payload: dict) -> requests.Response:
        """
        Method performs the POST request using the POST method from the Requests package
        :param endpoint: Еhe endpoint for which the request will be performed
        :param payload: The dict with the required data which will be posted
        :return: Response object (from Requests package)
        """
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            headers=self.request_headers,
            data=json.dumps(payload),
        )


class UserApiServices(ComonServices):

    def register_new_user(self, user_email: str, user_password: str) -> requests.Response:
        """
        Method make registration of a new user.
        It make the POST method to the "/register" endpoint, with the specific data
        :param user_email: The email with which will be registered a user
        :param user_password: The password with which the user will be registered
        :return: Response object (from Requests package)
        """
        user_payload = {"email": user_email, "password": user_password}
        return self.perform_post_requests(endpoint="/register", payload=user_payload)

    def create_new_user(self, user_name: str, user_jod: str) -> requests.Response:
        """
        Method makes creation/addition of a new user.
        It make the POST method to the "/register" endpoint, with the specific data
        :param user_name: The name with which will be created a user
        :param user_jod: The user's job with which the user will be created
        :return: Response object (from Requests package)
        """
        user_payload = {"name": user_name, "job": user_jod}
        return self.perform_post_requests(endpoint="/users", payload=user_payload)

