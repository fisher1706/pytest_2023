import pytest

from src.generators.plaer_localization import PlayerLocalization


def test_something_one(get_number):
    assert 1 == 1

    print(f"\nfrom get_number: {get_number}")


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_something_two(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("balance_value", [
    100,
    0,
    -10,
    "adssd"
])
def test_something_three(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_something_four(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_something_fifth(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number(15)
    ).build()
    print(object_to_send)
