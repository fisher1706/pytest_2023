import pytest


def get_cases():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("my_value", get_cases(), ids=str)
def test_my_magic_method(my_value):
    print(my_value)


@pytest.mark.parametrize("get_testing_scenarios",
                         ["scenario_2"],
                         indirect=True)
def test_data_indirect(get_testing_scenarios):
    print(get_testing_scenarios)


def test_magic_method(get_magic_method_two):
    print(get_magic_method_two(1))


def test_option(getting_env):
    print(f"\ndata: {getting_env}")
