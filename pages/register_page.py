"""Registration form: /register

A valid password on this page needs 8+ characters, upper and lower case,
a number, and a special character. Example: Bank@123
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/register")
        self.email = page.get_by_test_id("register-email")
        self.password = page.get_by_test_id("register-password")
        self.confirm_password = page.get_by_test_id("register-confirm-password")
        self.submit_button = page.get_by_test_id("register-submit")
        self.success_message = page.get_by_test_id("register-success")
        self.error_message = page.get_by_test_id("register-error")
        self.ready = self.email

    def register(self, email: str, password: str, confirm_password: str) -> None:
        self.email.fill(email)
        self.password.fill(password)
        self.confirm_password.fill(confirm_password)
        self.submit_button.click()

    def submit_empty(self) -> None:
        """Press Register with nothing typed. Used to check required-field errors."""
        self.submit_button.click()
