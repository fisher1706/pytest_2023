import requests

from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(POST_SCHEMA)
