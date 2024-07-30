import json

import requests


def test_can_create_new_user():
    """
    Test for creation of a new user
    """
    service_url = "https://reqres.in/"

    user_request_body = {"name": "valerie", "job": "AQA"}

    response = requests.post(
        url=f"{service_url}/api/user", headers={"Content-Type": "application/json"}, data=json.dumps(user_request_body)
    )

    assert response.status_code == 201


def test_can_register_new_user():
    """
    Test for registration of a user
    """
    user_request_body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

    response = requests.post(
        url="https://reqres.in/api/register",
        headers={"Content-Type": "application/json"},
        data=json.dumps(user_request_body),
    )

    assert response.status_code == 200
