"""
В контексте тестирования с помощью PyTest "хуки" и "фикстуры" - это два ключевых концепта,
которые помогают организовывать и выполнять тесты. Давай разберём их:

1. **Фикстуры (Fixtures)**:
 - Фикстуры в PyTest - это функции, которые предоставляют предварительно настроенные ресурсы для выполнения тестов.
 - Они могут использоваться для подготовки данных, установки тестового окружения, создания объектов и т. д.
 - Фикстуры могут быть определены в рамках модуля или внешнего файла conftest.py и могут быть параметризованы.

# Пример определения фикстуры:
"""


import pytest


class SomeResource:

    def cleanup(self):
        pass


@pytest.fixture
def some_resource():
    resource = SomeResource()
    # Предварительная настройка ресурса
    yield resource
    # Опциональное завершение работы с ресурсом после использования
    resource.cleanup()


"""
2. **Хуки (Hooks)**:
 - Хуки в PyTest - это специальные функции, которые выполняются автоматически на различных этапах выполнения тестов.
 - Они позволяют вам вмешиваться в процесс выполнения тестов и выполнять дополнительные действия перед и после тестов.
 - Позволяют настроить поведение PyTest до и после тестов, модулей, сессий и т. д.

# Пример использования хука:
"""


@pytest.hookimpl()
def pytest_runtest_setup(item):
    # Этот хук выполняется перед каждым тестом
    print("Setup for test:", item.name)


"""
Таким образом, основное различие между фикстурами и хуками заключается в их предназначении:
фикстуры предоставляют ресурсы для выполнения тестов,
тогда как хуки позволяют настраивать и управлять самим процессом выполнения тестов.
"""

"""
• pytest --fixtures - показывает все доступные fixture (встроенные, из плагинов и най-
денные в тестах и conftest.py). Добавление -v показывает в каких файлах находятся
fixture и на какой строке определена функция
• pytest --setup-show - показывает какие fixture запускаются и когдаbdd
"""