def test_can_register_new_user(user_api_services):
    """
    Test for registration of a user
    """

    response_status_code, response_model = user_api_services.register_new_user(
        user_email="eve.holt@reqres.in",
        user_password="cityslicka",
    )

    assert response_status_code == 200
    assert response_model.id == 4


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
