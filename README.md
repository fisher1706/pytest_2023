# validate response by pydantic -> use method - parse_obj of class BaseModel
# from pydantic import BaseModel, Field
# pydantic -> possibility write validators for field himself -> better use Field from pydantic

# @pytest.fixture -> create in conftest.py
# @pytest.mark.skip('[ISSUE-23414] Issue with network connection') -> skip test

# parameters with test start: -v - detalization -> -s - to see "print" in tests




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
pytest tests/
```

# to see list of all tests
```shell
pytest --collect-only
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
pytest --durations=0 -vv
```

# create Allure report -> add "--alluredir=allure_report_folder" -> "allure_report_folder" -> name of folder
```shell
pytest tests/ --alluredir=allure_report_folder
```

```shell
allure serve allure_report_folder
```