import pytest
import tables

from src.generators.plaer_localization import PlayerLocalization
from src.enums.user_enums import Statuses


def test_something_one(get_number):
    assert 1 == 1
    print(f"\nfrom get_number: {get_number}")


@pytest.mark.parametrize("status", [
    # "ACTIVE",
    # "BANNED",
    # "DELETED",
    # "INACTIVE"
    *Statuses.list()
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


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something_fifth(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc)
        .set_number(15)
        .build()
    ).build()
    print(object_to_send)


def test_get_data_films(get_db_session):
    data = get_db_session.query(tables.Films).first()
    print(f"\ntitle: {data.title}")


def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.ItemType, tables.ItemType.item_id == 3)


def test_try_to_add_test_data(get_db_session, get_add_method, get_item_type_generator):
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(f"\nnew_item_id: {item.item_id}")


def test_try_to_add_test_data_new(generate_item_type):
    print(f"\nnew_item_id: {generate_item_type.item_id}")
