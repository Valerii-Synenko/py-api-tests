import json
import os

from dotenv import load_dotenv

#  Load the environment config
load_dotenv()

import requests


class ComonServices:

    def __init__(self):
        self.base_url = os.getenv("BASE_API_URL")
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
