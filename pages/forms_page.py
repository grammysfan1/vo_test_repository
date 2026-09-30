"""Long practice form: /practice-forms

Date of birth has an id but no data-testid, so that one locator uses #forms-dob.
Everything else uses data-testid.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class FormsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/practice-forms")
        self.country = page.get_by_test_id("forms-country")
        self.title = page.get_by_test_id("forms-title")
        self.first_name = page.get_by_test_id("forms-first-name")
        self.last_name = page.get_by_test_id("forms-last-name")
        self.date_of_birth = page.locator("#forms-dob")
        self.date_of_joining = page.get_by_test_id("forms-doj")
        self.email = page.get_by_test_id("forms-email")
        self.phone_code = page.get_by_test_id("forms-phone-code")
        self.phone_number = page.get_by_test_id("forms-phone-number")
        self.contact_by_email = page.get_by_test_id("forms-comm-email")
        self.contact_by_phone = page.get_by_test_id("forms-comm-phone")
        self.submit_button = page.get_by_test_id("forms-submit")
        self.clear_button = page.get_by_test_id("forms-clear")
        self.success_message = page.get_by_test_id("forms-success")
        self.ready = self.first_name

    def submit(self) -> None:
        self.submit_button.click()

    def clear(self) -> None:
        self.clear_button.click()
