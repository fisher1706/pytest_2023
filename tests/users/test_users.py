import pytest
import time
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_user_list(get_users, get_number, say_hello, calculate, make_number):
    time.sleep(4)
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)

    print(f"\ncalculate: {calculate}")
    number = calculate(1, 1)
    print(f"result calculate: {number}")

    print(f"\nfrom get_number: {get_number}")
    print(f"\nfrom say_hello: {say_hello}")

    print(f"\nfixture_number: {make_number}")


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_another():
    """
    In that we try to check that 1 is equal 1
    :return:
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In this test we check calculator
    :param first_value:
    :param second_value:
    :param result:
    :param calculate:
    :return:
    """
    assert result == calculate(first_value, second_value)
