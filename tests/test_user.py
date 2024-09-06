import allure
from hamcrest import assert_that, equal_to, greater_than

from src.pydantic_models.request_models.update_user_request_model import UpdateUserRequest


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


@allure.title("Tes of the getting a user by its id")
@allure.description(
    "The test gets a user by its id, the check that the response status code is 200 and the name of the user"
)
def test_get_single_user(user_api_services):
    with allure.step("Step 1: Send GET request to get a user"):
        response_status_code, response_model = user_api_services.get_user_by_id(user_id=5)

    with allure.step("Step 1: Check that response status code is 200"):
        assert_that(response_status_code, equal_to(200))

    with allure.step("Step 3: Check the name of the user with ID 5"):
        assert_that(response_model.data.first_name, equal_to("Charles"))


@allure.title("Test verify getting a list of user from the specified page")
@allure.description(
    "The test gets a list of of users checks the status code and validate that there are 6 users inside the list."
)
def test_get_list_of_users(user_api_services):
    with allure.step("Step 1: Get list of users from the page #5"):
        response_status_code, response_model = user_api_services.get_list_of_users(page_number=2)

    with allure.step("Step 2: Check that response status code is 200"):
        assert_that(response_status_code, equal_to(200))

    with allure.step("Step 3: Check that there are 7 users inside the response list"):
        assert_that(len(response_model.data), equal_to(6))


@allure.title("Test verify updating a user via PATCH method")
@allure.description("The test sends PATCH method with required data and validate that the changes were made.")
def test_partially_update_user(user_api_services):

    with allure.step("Step 1: Send PATCH request with data to update"):
        user_model = UpdateUserRequest(name="Neo")
        response_status_code, user_response_model = user_api_services.update_user_by_patch_method(
            user_id=2, user_model=user_model
        )

    with allure.step("Step 2: Assert tar response status code is 200"):
        assert_that(response_status_code, equal_to(200))

    with allure.step("Step 3: Assert that the user name is updated"):
        assert_that(user_response_model.name, equal_to("Neo"))
