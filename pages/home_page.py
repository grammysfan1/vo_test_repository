"""The marketing home page: https://www.qapractice.com/"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/")
        # `ready` is the element that proves this screen has loaded.
        # Every page object in this project has one, so smoke tests stay short.
        self.heading = page.get_by_role(
            "heading", name="The Ultimate Automation Playground"
        )
        self.ready = self.heading
        # The site exposes this control as a button, even though it navigates.
        self.start_practicing_link = page.get_by_role(
            "button", name="Start Practicing", exact=True
        )

    def start_practicing(self):
        """Follow the main call-to-action to the list of practice sites."""
        self.start_practicing_link.click()
        # Imported here to avoid a loop: that page also imports other pages.
        from pages.practice_sites_page import PracticeSitesPage

        return PracticeSitesPage(self.page)
