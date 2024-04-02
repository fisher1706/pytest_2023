import pytest


@pytest.fixture()
def get_testing_scenarios(request):
    print(f"\nrequest.__dict__ =: {request.__dict__}")
    print(f"\nparam: {request.param}")

    if request.param == "production":
        return {"name": "John"}
    elif request.param == "scenario_2":
        return {"name": "Ann"}
    else:
        return {"name": "Anton"}


def _magic_method():
    return 17


@pytest.fixture()
def get_magic_method():
    return _magic_method


@pytest.fixture()
def get_magic_method_two(get_number):
    print(f"\nget number: {get_number}")

    def _wrapped(add_number):
        return add_number + get_number
    return _wrapped
