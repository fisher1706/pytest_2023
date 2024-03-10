import pytest
from src.LifeCoding.config.data import Data
from src.LifeCoding.pages.login_page import LoginPage
from src.LifeCoding.pages.dashboard_page import DashboardPage
from src.LifeCoding.pages.personal_page import PersonalPage


class BaseTest:
    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
