import pytest


def get_cases():
    return [1, 2, 3, 4, 5]


"""
отображение значения переменных переданных в тест "ids=str"
"""


@pytest.mark.parametrize("my_value", get_cases(), ids=str)
def test_my_magic_method(my_value):
    print(my_value)


"""
передача параметров в фикстуру "get_testing_scenarios" -> "request.param" -> indirect=True - прямое выполнение
если в "pytest_addoption" передали "production" - пропускаем тест
"""


@pytest.mark.parametrize(
    "get_testing_scenarios",
    ["production"],
    indirect=True
)
def test_data_indirect(get_testing_scenarios):
    print(get_testing_scenarios)


def test_magic_method(get_magic_method_two):
    print(get_magic_method_two(1))


"""
используется с фикстурой "getting_env"
можно изменять значения --env запуск через командную строку

pytest tests/something/experiments.py::test_option --env=production
"""


def test_option(getting_env):
    print(f"\nenv: {getting_env}")
