import pytest
import requests
from configuration import SERVICE_URL


@pytest.fixture()
def get_users():
    response = requests.get(url=SERVICE_URL)
    return response
