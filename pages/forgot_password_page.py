"""Forgot-password wizard: /forget-password

Three short steps, in this order:
1. email
2. secret code (practice code is in config.DEMO_SECRET_CODE)
3. current password, new password, confirm
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/forget-password")
        self.email = page.get_by_test_id("forgot-email")
        self.email_submit = page.get_by_test_id("forgot-email-submit")
        self.code = page.get_by_test_id("forgot-code")
        self.code_submit = page.get_by_test_id("forgot-code-submit")
        self.current_password = page.get_by_test_id("forgot-current-password")
        self.new_password = page.get_by_test_id("forgot-new-password")
        self.confirm_password = page.get_by_test_id("forgot-confirm-password")
        self.submit_button = page.get_by_test_id("forgot-submit")
        self.success_message = page.get_by_test_id("forgot-success")
        self.error_message = page.get_by_test_id("forgot-error")
        self.ready = self.email

    def request_reset(self, email: str) -> None:
        self.email.fill(email)
        self.email_submit.click()

    def enter_code(self, code: str) -> None:
        self.code.fill(code)
        self.code_submit.click()

    def set_new_password(self, current: str, new: str, confirm: str) -> None:
        self.current_password.fill(current)
        self.new_password.fill(new)
        self.confirm_password.fill(confirm)
        self.submit_button.click()
