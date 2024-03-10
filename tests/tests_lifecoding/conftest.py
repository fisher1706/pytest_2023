from pprint import pprint

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


"""
https://stackoverflow.com/questions/56856233/
what-role-does-request-cls-driver-have-in-pytest-fixture-with-a-scope-of-class

for [request.cls.driver = driver]
"""


@pytest.fixture()
def request_data(request):
    pprint(f"\nrequest_config:= {request.cls.__dict__}")
