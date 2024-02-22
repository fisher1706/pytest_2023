# validate response by pydantic -> use method - parse_obj of class BaseModel
# from pydantic import BaseModel, Field
# pydantic -> possibility write validators for field himself -> better use Field from pydantic

# @pytest.fixture -> create in conftest.py


# to see help
```shell
pytest -h
```

# to run test_getting_user_list
```shell
pytest tests/something_test.py::test_getting_user_list
```

# to run test_getting_user_list with "--setup-show" -> to see started fixtures
```shell
pytest --setup-show tests/something_test.py::test_getting_user_list
```

# to run test_another "--setup-show" -> to see started fixtures
```shell
pytest --setup-show tests/something_test.py::test_another
```

# to see all fixtures for test_getting_user_list
```shell
pytest --fixtures tests/something_test.py::test_getting_user_list
```

# to see all fixtures for test_another
```shell
pytest --fixtures -v tests/something_test.py::test_another
```


# to run all tests from dir "tests"
```shell
pytest tests/
```