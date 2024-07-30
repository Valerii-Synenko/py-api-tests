import json

import requests

from src.services import UserApiServices


def test_can_register_new_user():
    """
    Test for registration of a user
    """
    user_registration_response = UserApiServices().register_new_user(
        {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    )

    assert user_registration_response.status_code == 200
