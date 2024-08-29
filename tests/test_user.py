import allure
from hamcrest import assert_that, equal_to, greater_than


@allure.title("Test of the registration of a new user")
@allure.description(
    """Tests that a new user can be successfully registered with valid email and password.
    Verifies that the API returns a 200 status code and that the user ID is correctly assigned."""
)
def test_can_register_new_user(user_api_services):
    """ """
    with allure.step("Step 1: Register new user."):
        response_status_code, response_model = user_api_services.register_new_user(
            email="eve.holt@reqres.in",
            password="pistol",
        )

    with allure.step("Step 2: Check that response status code is 201."):
        assert_that(response_status_code, equal_to(200))

    with allure.step("Step 3: Check that the response has id 4"):
        assert_that(response_model.id, equal_to(4))


@allure.title("Test of the creation of a new user")
@allure.description(
    """Tests that a new user can be created with random name and job using the Faker library.
    Verifies that the API returns a 201 status code and that the username is not empty."""
)
def test_can_create_new_user(user_api_services, faker):
    with allure.step("Step 1: Create a new user."):
        response_status_code, response_model = user_api_services.create_new_user(
            name=faker.name(),
            job=faker.job(),
        )

    with allure.step("Step 2: Check that response status code is 201."):
        assert_that(response_status_code, equal_to(201))

    with allure.step("Step 3: Check that the user name length in the response is not null."):
        assert_that(len(response_model.name), greater_than(0))
