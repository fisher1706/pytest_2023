import pytest


def get_cases():
    return [1, 2, 3, 4, 5]


# TODO: "ids=str" for indicate value in tests results
@pytest.mark.parametrize("my_value", get_cases(), ids=str)
def test_my_magic_method(my_value):
    print(my_value)


# TODO: send data in fixture "indirect=True" - direct execution
@pytest.mark.parametrize("get_testing_scenarios",
                         ["scenario_2"],
                         indirect=True
                         )
def test_data_indirect_one(get_testing_scenarios):
    print(get_testing_scenarios)


@pytest.mark.parametrize("get_testing_scenarios",
                         ["scenario_1"],
                         indirect=True
                         )
def test_data_indirect_two(get_testing_scenarios):
    print(get_testing_scenarios)


def test_magic_method(get_magic_method_two):
    print(get_magic_method_two(1))


# TODO: start tests: pytest tests/something/experiments.py --env=prod or addopts = -s -v --env=prod [pytest.ini]
def test_option(getting_env):
    print(f"\ndata: {getting_env}")
