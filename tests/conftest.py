import pytest
from faker import Faker

from src.services import UserApiServices


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def user_ppi_services():
    return UserApiServices()
