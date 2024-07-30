import json

import requests


def test_can_create_new_user():
    service_url = "https://reqres.in/"

    user_request_body = {"name": "valerie", "job": "AQA"}

    response = requests.post(
        url=f"{service_url}/api/user", headers={"Content-Type": "application/json"}, data=json.dumps(user_request_body)
    )

    assert response.status_code == 201


def test_can_register_new_user():
    user_request_body = {
        "email": "val.erie@reqres.in",
        "password": "StrongPWD"
    }

    response = requests.post(
        url="https://reqres.in/api/register",
        headers={"Content-Type": "application/json"},
        data=json.dumps(user_request_body)
    )

    print(response)

    assert response.status_code == 200



