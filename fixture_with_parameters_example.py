import pytest


# Basic Example
@pytest.fixture(params=[1, 2, 3])
def number(request):
    # request.param gives you the current parameter value
    return request.param

def test_is_positive(number):
    assert number > 0


# Fixture Parameters with Complex Data
@pytest.fixture(params=[
    {"username": "alice", "password": "123"},
    {"username": "bob", "password": "abc"}
])
def user_data(request):
    print(f"User data: {request.param}")
    return request.param


def test_login(user_data):
    assert "username" in user_data
    assert len(user_data["password"]) >= 3


# Combining Parameterized Fixtures and Parametrize Decorator
@pytest.fixture(params=["mysql", "postgres"])
def db_engine(request):
    return request.param

@pytest.mark.parametrize("version", ["5.7", "8.0"])
def test_db_setup(db_engine, version):
    print(f"Testing {db_engine} version {version}")

