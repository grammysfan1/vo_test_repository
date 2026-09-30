"""Home page navigation.

Arrange: open the page.
Act:     click one thing.
Assert:  check what the user should see next.

allure.step(...) is the line that shows up in the report.
"""

import re

import allure
from playwright.sync_api import expect

from pages.home_page import HomePage


@allure.feature("Navigation")
@allure.story("Home page")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Start Practicing opens the practice list")
def test_start_practicing_opens_the_practice_list(page):
    home = HomePage(page)

    with allure.step("Open the home page"):
        home.open()

    with allure.step("Click Start Practicing"):
        practice_sites = home.start_practicing()

    with allure.step("The practice list is open"):
        expect(practice_sites.heading).to_be_visible()
        expect(page).to_have_url(re.compile(r".*/practice-page-selection$"))
