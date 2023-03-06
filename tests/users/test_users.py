from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_user_list(get_users, get_number, say_hello, calculate, make_number):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)

    print(f"\ncalculate: {calculate}")
    number = calculate(1, 1)
    print(f"result calculate: {number}")

    print(f"\nfrom get_number: {get_number}")
    print(f"\nfrom say_hello: {say_hello}")

    print(f"\nfixture_number: {make_number}")


def test_another():
    assert 1 == 1
