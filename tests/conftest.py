import pytest
from faker import Faker

from src.services.user_api_services import UserApiServices


@pytest.fixture
def faker():
    """
    The fixture that provides the object of the Faker.
    The Fake is the object needs to generate of randomly fake data.
    :return: The Faker object
    """
    return Faker()


@pytest.fixture
def user_api_services():
    """
    The fixture that provides the object of the UserApiServices class
    :return: the object of the UserApiServices class
    """
    return UserApiServices()
