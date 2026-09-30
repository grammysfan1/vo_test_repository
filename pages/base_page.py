"""The parent of every page object.

KISS idea: put shared things here once (open the page, use the header).
Put things that belong to one screen in that screen's class.
"""

from playwright.sync_api import Page

from config import BASE_URL


class BasePage:
    def __init__(self, page: Page, path: str) -> None:
        self.page = page
        # path is the part after the domain, for example "/register".
        self.path = path

        # The same header is on every screen, so the locators live here.
        # #qapractice-navbar keeps us off the same words in the footer.
        nav = page.locator("#qapractice-navbar")
        self.practice_sites_link = nav.get_by_role("link", name="Practice Sites")
        self.interview_link = nav.get_by_role("link", name="Interview Prep")
        self.about_link = nav.get_by_role("link", name="About")
        self.contact_link = nav.get_by_role("link", name="Contact")

    def open(self) -> None:
        """Go to this screen. Call this at the start of a test."""
        self.page.goto(f"{BASE_URL}{self.path}")

    def open_practice_sites(self) -> None:
        self.practice_sites_link.click()

    def open_contact(self) -> None:
        self.contact_link.click()
