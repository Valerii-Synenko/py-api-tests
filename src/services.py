import json

import requests


class ComonServices:

    def __init__(self):
        self.base_url = "https://reqres.in/api"
        self.request_headers = {"Content-Type": "application/json"}

    def perform_post_requests(self, endpoint: str, user_payload: dict) -> requests.Response:
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            headers=self.request_headers,
            data=json.dumps(user_payload),
        )


class UserApiServices(ComonServices):

    def register_new_user(self, user_payload) -> requests.Response:
        return self.perform_post_requests(endpoint="/register", user_payload=user_payload)

    def create_new_user(self, user_payload) -> requests.Response:
        return self.perform_post_requests(endpoint="/users", user_payload=user_payload)

