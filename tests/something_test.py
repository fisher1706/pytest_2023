from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_user_list(get_users, say_hello):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)

    print('\n', say_hello)


def test_another():
    assert 1 == 1
