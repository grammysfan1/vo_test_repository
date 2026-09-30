"""Login behaviour. Credentials come from config.py, not from the test body.

That way a student changes the demo account in one file.
The @allure.feature label groups these four tests in the report.
"""

import re

import allure
from playwright.sync_api import expect

from config import DEMO_EMAIL, DEMO_PASSWORD
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Demo account shows a success message")
def test_valid_login_shows_success(page):
    login = LoginPage(page)

    with allure.step("Open the login page"):
        login.open()

    with allure.step("Sign in with the demo account"):
        login.login(DEMO_EMAIL, DEMO_PASSWORD)

    with allure.step("Success message is shown"):
        expect(login.success_message).to_contain_text("Login Successful")


@allure.feature("Login")
@allure.story("Validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Empty form asks for email and password")
def test_empty_login_asks_for_both_fields(page):
    login = LoginPage(page)

    with allure.step("Open the login page"):
        login.open()

    with allure.step("Submit without typing"):
        login.submit_button.click()

    with allure.step("Both fields are required"):
        expect(login.error_message).to_contain_text("Email and Password are required")


@allure.feature("Login")
@allure.story("Invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Wrong password shows an error")
def test_wrong_password_shows_an_error(page):
    login = LoginPage(page)

    with allure.step("Open the login page"):
        login.open()

    with allure.step("Sign in with a wrong password"):
        login.login(DEMO_EMAIL, "wrong-password")

    with allure.step("An error is shown"):
        expect(login.error_message).to_contain_text("Invalid email id and password")


@allure.feature("Login")
@allure.story("Links")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Register link opens the registration page")
def test_register_link_opens_registration(page):
    login = LoginPage(page)

    with allure.step("Open the login page"):
        login.open()

    with allure.step("Click Register now"):
        register = login.go_to_register()

    with allure.step("The registration form is open"):
        expect(register.email).to_be_visible()
        expect(page).to_have_url(re.compile(r".*/register$"))
