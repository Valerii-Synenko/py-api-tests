import requests


class AssertableResponse:

    def __init__(self, response: requests.Response):
        self._response = response

    def check_status_code(self, expected_status_code: int):
        """
        The method that asserts that the received status code is equal to expect one
        :param expected_status_code: The code that you expect to receive
        :return: None
        """
        assert self._response.status_code == expected_status_code

    def check_response_body_field(self, required_field: str, expected_value: any):
        """
        The method asserts that a field has expected value
        :param required_field: The required field title
        :param expected_value: The expected field value
        :return: None
        """
        assert self._response.json()[required_field] == expected_value
