import json
import os
import sys
from typing import Any

import allure
import requests
from dotenv import load_dotenv
from logbook import Logger, StreamHandler
from requests import HTTPError, RequestException, Timeout

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
        self.logger = Logger("ApiService")  # Add logbook logger
        self.logger.handlers.append(StreamHandler(sys.stdout))  # Add StreamHandler to output logs to console

    @allure.step("Perform POST request")
    def _post(self, endpoint: str, payload: dict, timeout: int = 20) -> requests.Response:
        """
        Sends a POST request to the specified endpoint with the given payload.

        This method utilizes the Requests package to perform the POST request, including the common headers
        and base URL defined in the class.

        :param endpoint: The API endpoint to which the POST request will be sent.
        :param payload: A dictionary containing the data to be sent in the POST request body.
        :return: A Response object from the Requests package representing the server's response.
        """
        self.logger.info(
            f"""
                Going to send POST request:
                url: {self.base_url}{endpoint},
                headers: {self.request_headers},
                body: {json.dumps(payload)}
                """
        )

        try:
            response = requests.post(
                url=f"{self.base_url}{endpoint}",
                headers=self.request_headers,
                data=json.dumps(payload),
                timeout=timeout,
            )
            response.raise_for_status()
            self.logger.info(
                f"""
                The response was received:
                Status code is: {response.status_code}.
                Response body: {response.text}\n
                """
            )

        except (HTTPError, Timeout, ConnectionError) as e:
            self.logger.error(f"HTTP Request failed: {e}")
            raise
        except RequestException as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise

        return response

    @allure.step("Perform GET request")
    def _get(self, endpoint: str, params: Any | None = None, timeout: int = 20) -> requests.Response:
        """
        Performs a GET request to the specified endpoint.

        :param endpoint: The API endpoint to send the GET request to.
        :param timeout: Timeout in seconds for the request. Defaults to 20.

        :return: The response object from the GET request.

        :raise:
            HTTPError: If the response contains an HTTP error status.
            Timeout: If the request times out.
            ConnectionError: If a connection error occurs.
            RequestException: For any other request-related exceptions.
        """
        self.logger.info(
            f"Going to send GET request:\n"
            f"url: {self.base_url}{endpoint},\n"
            f"params: {params},\n"
            f"headers: {self.request_headers}\n"
        )
        try:
            response = requests.get(
                url=f"{self.base_url}{endpoint}",
                headers=self.request_headers,
                params=params,
                timeout=timeout,
            )
            response.raise_for_status()
            self.logger.info(
                f"The response was received:\n"
                f"Status code: {response.status_code}\n"
                f"Response body: {response.text}\n"
            )

        except (HTTPError, Timeout, ConnectionError) as e:
            self.logger.error(f"HTTP Request failed: {e}")
            raise
        except RequestException as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise

        return response

    @allure.step("Perform PATCH request")
    def _patch(self, endpoint: str, payload: dict, timeout: int = 20) -> requests.Response:
        """
        Sends a PATCH request to the specified endpoint with the given payload.

        This method utilizes the Requests package to perform the PATCH request, including the common headers
        and base URL defined in the class.

        :param endpoint: The API endpoint to which the PATCH request will be sent.
        :param payload: A dictionary containing the data to be sent in the PATCH request body.
        :return: A Response object from the Requests package representing the server's response.
        """
        self.logger.info(
            f"""
                Going to send PATCH request:
                url: {self.base_url}{endpoint},
                headers: {self.request_headers},
                body: {json.dumps(payload)}
                """
        )

        try:
            response = requests.patch(
                url=f"{self.base_url}{endpoint}",
                headers=self.request_headers,
                data=json.dumps(payload),
                timeout=timeout,
            )
            response.raise_for_status()
            self.logger.info(
                f"""
                The response was received:
                Status code is: {response.status_code}.
                Response body: {response.text}\n
                """
            )

        except (HTTPError, Timeout, ConnectionError) as e:
            self.logger.error(f"HTTP Request failed: {e}")
            raise
        except RequestException as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise

        return response

    @allure.step("Perform PUT request")
    def _put(self, endpoint: str, payload: dict, timeout: int = 20) -> requests.Response:
        """
        Sends a PUT request to the specified endpoint with the given payload.

        This method utilizes the Requests package to perform the PUT request, including the common headers
        and base URL defined in the class.

        :param endpoint: The API endpoint to which the PUT request will be sent.
        :param payload: A dictionary containing the data to be sent in the PUT request body.
        :param timeout: Timeout in seconds for the PUT request (default: 20 seconds).
        :return: A Response object from the Requests package representing the server's response.
        """
        self.logger.info(
            f"""
                Going to send PUT request:
                url: {self.base_url}{endpoint},
                headers: {self.request_headers},
                body: {json.dumps(payload)}
                """
        )

        try:
            response = requests.put(
                url=f"{self.base_url}{endpoint}",
                headers=self.request_headers,
                data=json.dumps(payload),
                timeout=timeout,
            )
            response.raise_for_status()
            self.logger.info(
                f"""
                The response was received:
                Status code is: {response.status_code}.
                Response body: {response.text}\n
                """
            )

        except (HTTPError, Timeout, ConnectionError) as e:
            self.logger.error(f"HTTP Request failed: {e}")
            raise
        except RequestException as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise

        return response

    @allure.step("Perform DELETE request")
    def _delete(self, endpoint: str, timeout: int = 20) -> requests.Response:
        """
        Sends a DELETE request to the specified endpoint.

        This method uses the Requests package to perform the DELETE request, including the common headers
        and base URL defined in the class.

        :param endpoint: The API endpoint to which the DELETE request will be sent.
        :return: A Response object from the Requests package representing the server's response.
        """
        self.logger.info(
            f"""
                Going to send DELETE request:
                url: {self.base_url}{endpoint},
                headers: {self.request_headers},
                """
        )

        try:
            response = requests.delete(
                url=f"{self.base_url}{endpoint}",
                headers=self.request_headers,
                timeout=timeout,
            )
            response.raise_for_status()
            self.logger.info(
                f"""
                The response was received:
                Status code is: {response.status_code}.
                """
            )

        except (HTTPError, Timeout, ConnectionError) as e:
            self.logger.error(f"HTTP Request failed: {e}")
            raise
        except RequestException as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise

        return response
