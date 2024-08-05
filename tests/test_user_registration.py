from src.pydantic_models.response_models.user_response_model import CreateUserResponseModel


def test_can_register_new_user(user_api_services):
    """
    Test for registration of a user
    """

    user_register_model = CreateUserResponseModel(

    )
    user_registration_response = user_api_services.register_new_user(
        user_email="eve.holt@reqres.in",
        user_password="cityslicka",
    )

    user_registration_response.check_response_body_field(required_field="id", expected_value=4)


def test_can_create_new_user(user_api_services, faker):
    """
    Test for creation of a user
    """

    response_status_code, response_model = user_api_services.create_new_user(
        user_name=faker.name(),
        user_job=faker.job(),
    )

    assert response_status_code == 201

    assert len(response_model.name) > 0

