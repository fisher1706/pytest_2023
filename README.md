# validate response by pydantic -> use method - [parse_obj] - old or [model_validate] - new of class BaseModel
# from pydantic import BaseModel, Field
# pydantic -> possibility write validators for field himself -> better use Field from pydantic

# @pytest.fixture -> create in conftest.py
# @pytest.mark.skip('[ISSUE-23414] Issue with network connection') -> skip test

# parameters with test start: 
            -v - detalization
            -s - to see "print" in tests
            -vv - all information

# to see help
```shell
pytest -h
```

# to run test "test_getting_user_list"
```shell
pytest tests/users/test_users.py::test_getting_user_list
```

# to run test "test_getting_user_list with" with parameter "--setup-show" -> to see started fixtures
```shell
pytest --setup-show tests/users/test_users.py::test_getting_user_list
```

# to see all fixtures for file "test_users.py"
```shell
pytest --fixtures tests/users/test_users.py
```

# to run all tests from dir "tests"
```shell
pytest tests/*
```

# to see list of all tests
```shell
pytest --collect-only
```

# stop all tests after first failed test
```shell
pytest --maxfail=1
```

# run tests with mark
# create markers -> 1. create descriptions in file "pytest.ini"
                    markers =
                            development: marker for running test only dev env.
                            production: marker for running test on pro env.
#                   2. @pytest.mark.development

# run tests with mark "development"
```shell
pytest -k development
```

# run tests without mark "development"
```shell
pytest -k "not development"
```

# to see time of tests -> --durations=n - mark all tests with test time > n -> 0 - only for example -> -vv -> to see all
```shell
pytest --durations=1 -vv
```

# -----------------------------------------ALLURE-----------------------------------------------------------------------
# install allure before

# create Allure report -> add "--alluredir=allure_report_folder" -> "allure_report_folder" -> name of folder
```shell
pytest tests/ --alluredir=allure-results
```

```shell
allure serve allure-results
```

# -------------------------------------------PYTEST.INI-----------------------------------------------------------------
# addopts= -s -v -> add in "pytest.ini" -> all tests start with parameter -v -s

# ------------------------------------------HOOKS-----------------------------------------------------------------------
# hooks -> methods in conftest.py -> run "before" and "after" tests

# start test use hook "pytest_addoption"
```shell
pytest tests/something/experiments.py::test_option --env=production
```

# -----------------------------------------PYTEST WORK------------------------------------------------------------------
# 1. Configuration 
# 2. Collection 
# 3. Running 
# 4. Reporting 

# ------------------------------------------DOCKER----------------------------------------------------------------------
# Эту команду мы запускаем, чтобы собрать наш контейнер
```shell
#docker build --build-arg env=development -t automation-tests .
docker build -t automation-tests .
```

# Эта команда нужна, чтобы запустить наш созданный контейнер
```shell
docker run automation-tests
```

# Эти 2 команды нам нужны чтобы скопировать данные из контейнера и чтобы сгенерировать из результата репорт
```shell
docker cp $(docker ps -a -q | head -1):/usr/lessons/allure-results .
allure serve allure-results
```

# Две команды ниже, помогут вам в экспериментах, чтобы после них почистить свой компьютер
```shell
docker rm $(docker ps -aq)
```

# Пробрасываем параметры в фикстуру
```shell
pytest tests/something/experiments.py::test_option --env=production
```

# ------------------------------------------SOME_HOOK_EXAMPLE-----------------------------------------------------------
```shell
pytest tests/hooks_example_three/test_hooks_three.py
```

# start tests from docker-compose
```shell
docker-compose build && docker-compose up
```

# Для параллельного запуска тестов используй плагин pytest-xdist, устанавливается как обычный пакет:
# $ pip install pytest-xdist
# Опция -n/--numprocesses задает количество процессов:
# $ pytest -n8