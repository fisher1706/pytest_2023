import requests

from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_user_list():
    response = requests.get(SERVICE_URL)
    print(f"\nresponse_json:= {response.json()}, \nstatus_code:= {response.status_code}")
    test_object = Response(response)
    test_object.assert_status_code(300).validate(User)
