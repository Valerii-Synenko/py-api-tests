

def test_can_register_new_user(user_ppi_services):
    """
    Test for registration of a user
    """
    user_registration_response = user_ppi_services.register_new_user(
        user_email="eve.holt@reqres.in",
        user_password="cityslicka",
    )

    assert user_registration_response.json()["id"] == 4

    assert user_registration_response.status_code == 200


def test_can_create_new_user(user_ppi_services, faker):
    """
    Test for creation of a user
    """
    user_creation_response = user_ppi_services.create_new_user(
        user_name=faker.name(),
        user_jod=faker.job(),
    )

    assert user_creation_response.json()["name"] is not None

    assert user_creation_response.status_code == 201
