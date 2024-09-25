import pytest

from Centime.PageObjects.login_page import LoginPage
from Centime.utils import config


def test_register_and_login(driver):  # No spaces between 'driver'
    login_page = LoginPage(driver)
    login_page.open(config.baseurl)

    # Register
    login_page.register(config.email, config.password)

    # Login
    login_page.login(config.email, config.password)

    # Check login status (Verify elements specific to logged-in users)
    assert "My Account" in driver.page_source
