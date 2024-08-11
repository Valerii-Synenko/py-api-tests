import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class ComonServices:
    """
    A base class for all service classes, providing common functionality such as the base URL for requests
    and shared headers.

    This class includes attributes and methods that are common across multiple service classes, such as
    setting the base URL and defining headers used in HTTP requests.
    """

    def __init__(self):
        self.base_url = os.getenv("BASE_API_URL")
        self.request_headers = {"Content-Type": "application/json"}

    def perform_post_requests(self, endpoint: str, payload: dict) -> requests.Response:
        """
        Sends a POST request to the specified endpoint with the given payload.

        This method utilizes the Requests package to perform the POST request, including the common headers
        and base URL defined in the class.

        :param endpoint: The API endpoint to which the POST request will be sent.
        :param payload: A dictionary containing the data to be sent in the POST request body.
        :return: A Response object from the Requests package representing the server's response.
        """
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            headers=self.request_headers,
            data=json.dumps(payload),
        )
