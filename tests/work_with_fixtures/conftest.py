import datetime
import json

import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    """
    идентификатор узла (nodeid) может иметь двоеточия
    ключи становятся именами файлов внутри .cache
    меняем двоеточия на что-то безопасное в имени файла
    """

    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        error_string = "длительность теста превышает последний боле чем в 2-а раза "
        assert this_duration <= last_duration * 2, error_string
