import pytest
from random import randrange

# import tables
from src.generators.player import Player
from src.generators.item_type_generator import ItemsTypeBuilder
# from db import Session


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


@pytest.fixture()
def get_player_generator():
    return Player()


"""
to create db_session
"""


# @pytest.fixture()
# def get_db_session():
#     session = Session()
#     try:
#         yield session
#     finally:
#         session.close()


def delete_test_data(session, table, filter_data):
    print(f"\nfilter_data:= {filter_data}")
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    print(f"\nitem:= {item}")
    session.add(item)
    session.commit()


"""
fixture: delete data from db
"""


@pytest.fixture()
def get_delete_method():
    return delete_test_data


"""
fixture: add data to db
"""


@pytest.fixture()
def get_add_method():
    return add_method


@pytest.fixture()
def get_item_type_generator():
    return ItemsTypeBuilder()


# @pytest.fixture()
# def generate_item_type(get_db_session, get_item_type_generator, get_add_method, get_delete_method):
#     item = tables.ItemType(**get_item_type_generator.build())
#     get_add_method(get_db_session, item)
#     yield item
#     get_delete_method(get_db_session, tables.ItemType, tables.ItemType.item_id == item.item_id)
#     print(f"delete from: {tables.ItemType} - id: {item.item_id}")


"""
добавляет новые параметры к тесту -> pytest_addoption + getting_env
для этого используем hook - add_options
arg parser -> парсинг данных из командной строки

1. добавляем хуком "pytest_addoption" переменную "environment" в "pytestconfig" - для "разделения тестов"
"""


def pytest_addoption(parser):
    print("\nstart addoption")
    print(f"\nparser=: {parser.__dict__}")
    parser.addoption(
        '--env',
        default='development',
        choices=("development", "production"),
        help='It is env variable where our tests_lifecoding will be run. '
             'Possible values: '
             'development(default), '
             'production '
    )


"""
читает значение --env заданное hook add_options
"""


@pytest.fixture(autouse=True)
def getting_env(request):
    """
    description of fixture
    """
    print(f"\nrequest_option:= {request.config.getoption}")
    env = request.config.getoption('--env')
    yield env
