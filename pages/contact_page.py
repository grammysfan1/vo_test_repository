"""Contact form: /contact"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/contact")
        self.name = page.get_by_test_id("contact-name")
        self.email = page.get_by_test_id("contact-email")
        self.topic = page.get_by_test_id("contact-topic")
        self.message = page.get_by_test_id("contact-message")
        self.submit_button = page.get_by_test_id("contact-submit")
        self.name_error = page.get_by_test_id("contact-name-error")
        self.email_error = page.get_by_test_id("contact-email-error")
        self.message_error = page.get_by_test_id("contact-message-error")
        self.success_message = page.get_by_test_id("contact-success")
        self.ready = self.name

    def send(self, name: str, email: str, message: str, topic: str | None = None) -> None:
        self.name.fill(name)
        self.email.fill(email)
        if topic:
            self.topic.select_option(topic)
        self.message.fill(message)
        self.submit_button.click()
