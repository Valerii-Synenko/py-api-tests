def test_can_register_new_user(user_ppi_services):
    """
    Test for registration of a user
    """
    user_registration_response = user_ppi_services.register_new_user(
        user_email="eve.holt@reqres.in",
        user_password="cityslicka",
    )

    user_registration_response.check_response_body_field(required_field="id", expected_value=4)


def test_can_create_new_user(user_ppi_services, faker):
    """
    Test for creation of a user
    """
    user_creation_response = user_ppi_services.create_new_user(
        user_name=faker.name(),
        user_jod=faker.job(),
    )

    user_creation_response.check_status_code(201)
