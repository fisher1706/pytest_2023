import pytest
from random import randrange


@pytest.fixture(scope='session')
def say_hello():
    print('\nhello')
    return 14


@pytest.fixture()
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def make_number():
    print("\nI`m getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"\nNumber at home {number}")
