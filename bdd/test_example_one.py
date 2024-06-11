import pytest
from pytest_bdd import scenarios, given, when, then

# Загружаем все сценарии из указанного .feature файла
scenarios('features/example.feature')


@pytest.fixture
def sample_fixture():
    return {"key": "value"}


@given('a sample fixture is available')
def a_sample_fixture_is_available(sample_fixture):
    pass


@when('I use the fixture')
def i_use_the_fixture(sample_fixture):
    sample_fixture['key'] = 'new_value'


@then('it should behave correctly')
def it_should_behave_correctly(sample_fixture):
    assert sample_fixture['key'] == 'new_value'
 