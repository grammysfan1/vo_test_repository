"""Login form: /practice-login-form

Locators use data-testid. This site adds that attribute on purpose,
so a test does not break when someone changes a CSS class.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/practice-login-form")
        self.email = page.get_by_test_id("login-email")
        self.password = page.get_by_test_id("login-password")
        self.remember_me = page.get_by_test_id("login-remember")
        self.submit_button = page.get_by_test_id("login-submit")
        self.forgot_password_link = page.get_by_test_id("login-forgot-password")
        self.register_link = page.get_by_test_id("login-register")
        # These two appear only after submit. That is expected.
        self.success_message = page.get_by_test_id("login-success")
        self.error_message = page.get_by_test_id("login-error")
        self.ready = self.email

    def login(self, email: str, password: str) -> None:
        """Type the credentials and press Sign in.

        The test decides what "success" means. This method only does the action.
        """
        self.email.fill(email)
        self.password.fill(password)
        self.submit_button.click()

    def go_to_register(self):
        self.register_link.click()
        from pages.register_page import RegisterPage

        return RegisterPage(self.page)

    def go_to_forgot_password(self):
        self.forgot_password_link.click()
        from pages.forgot_password_page import ForgotPasswordPage

        return ForgotPasswordPage(self.page)
