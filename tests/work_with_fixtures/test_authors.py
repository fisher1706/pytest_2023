"""Некоторые тесты, использующие временные файлы данных."""

import json


def test_brian_in_portland(author_file_json):
    """Тест, использующий файл данных."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Для обоих тестов используется один и тот же файл."""
    with author_file_json.open() as f:
        authors = json.load(f)
        print(f"authors: {authors}")

    for a in authors:
        print(f"a: {a}")
        assert len(authors[a]['City']) > 0
