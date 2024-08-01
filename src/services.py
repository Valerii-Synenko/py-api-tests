import json

import requests


class ComonServices:

    def __init__(self):
        self.base_url = "https://reqres.in/api"
        self.request_headers = {"Content-Type": "application/json"}

    def perform_post_requests(self, endpoint: str, payload: dict) -> requests.Response:
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            headers=self.request_headers,
            data=json.dumps(payload),
        )


class UserApiServices(ComonServices):

    def register_new_user(self, user_email: str, user_password: str) -> requests.Response:
        user_payload = {"email": user_email, "password": user_password}
        return self.perform_post_requests(endpoint="/register", payload=user_payload)

    def create_new_user(self, user_name: str, user_jod: str) -> requests.Response:
        user_payload = {"name": user_name, "job": user_jod}
        return self.perform_post_requests(endpoint="/users", payload=user_payload)

