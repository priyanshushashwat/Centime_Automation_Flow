import pytest

from Centime.PageObjects.profile_page import ProfilePage
from Centime.utils import config


def test_add_address(driver):
    profile_page = ProfilePage(driver)
    profile_page.add_address(config.first_name, config.last_name, config.address)

    # Verify the address was saved
    assert profile_page.verify_address_saved(config.address)
