def test_can_register_new_user(user_api_services):
    """
    Tests that a new user can be successfully registered with valid email and password.

    Verifies that the API returns a 200 status code and that the user ID is correctly assigned.
    """
    response_status_code, response_model = user_api_services.register_new_user(
        email="eve.holt@reqres.in",
        password="pistol",
    )

    assert response_status_code == 200
    assert response_model.id == 4


def test_can_create_new_user(user_api_services, faker):
    """
    Tests that a new user can be created with random name and job using the Faker library.

    Verifies that the API returns a 201 status code and that the username is not empty.
    """
    response_status_code, response_model = user_api_services.create_new_user(
        name=faker.name(),
        job=faker.job(),
    )

    assert response_status_code == 201
    assert len(response_model.name) > 0
