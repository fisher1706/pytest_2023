# validate response by pydantic -> use method - parse_obj of class BaseModel
# from pydantic import BaseModel, Field
# pydantic -> possibility write validators for field himself -> better use Field from pydantic


# to see help
```shell
pytest -h
```

# to run test_getting_posts
```shell
pytest tests/something_test.py::test_getting_posts
```

# to run all tests from dir "tests"
```shell
pytest tests/
```