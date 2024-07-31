from src.services import UserApiServices


def test_can_register_new_user():
    """
    Test for registration of a user
    """
    user_registration_response = UserApiServices().register_new_user(
        user_email="eve.holt@reqres.in",
        user_password="cityslicka",
    )

    assert user_registration_response.status_code == 200


def test_can_create_new_user():
    """
    Test for creation of a user
    """
    user_creation_response = UserApiServices().create_new_user(
        user_name="morpheus",
        user_jod="leader",
    )

    assert user_creation_response.status_code == 201
