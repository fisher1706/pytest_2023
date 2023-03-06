import pytest
import requests
from configuration import SERVICE_URL


@pytest.fixture(scope='session')
def say_hello():
    print('\nhello')
    return 14


@pytest.fixture()
def get_users():
    response = requests.get(url=SERVICE_URL)
    return response
