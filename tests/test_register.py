"""A small registration check.

We only cover the empty form here. A full happy-path test would
also need a unique email and a password that meets the rules
documented on RegisterPage.
"""

import allure
from playwright.sync_api import expect

from pages.register_page import RegisterPage


@allure.feature("Registration")
@allure.story("Validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Empty form requires an email")
def test_empty_register_requires_an_email(page):
    register = RegisterPage(page)

    with allure.step("Open the registration page"):
        register.open()

    with allure.step("Submit the empty form"):
        register.submit_empty()

    with allure.step("Email is required"):
        expect(register.error_message).to_contain_text("Email is required")
