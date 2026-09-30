"""The hub that links to each practice exercise.

Several cards share the label "Start practising", so we click by href.
The address in the link is stable. The button text is not unique.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.contact_page import ContactPage
from pages.flight_booking_page import FlightBookingPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.forms_page import FormsPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.shop_page import ShopPage
from pages.ui_elements_page import UiElementsPage


class PracticeSitesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/practice-page-selection")
        self.heading = page.get_by_role("heading", name="Practice Sites")
        self.ready = self.heading

    def _open_card(self, href: str) -> None:
        self.page.locator(f"a[href='{href}']").click()

    def open_login(self) -> LoginPage:
        self._open_card("/practice-login-form")
        return LoginPage(self.page)

    def open_forms(self) -> FormsPage:
        self._open_card("/practice-forms")
        return FormsPage(self.page)

    def open_shop(self) -> ShopPage:
        # The site spells this path "ecommerece". Keep the typo: it is the real URL.
        self._open_card("/practice-ecommerece-website")
        return ShopPage(self.page)

    def open_flights(self) -> FlightBookingPage:
        self._open_card("/flight-booking-scenarios")
        return FlightBookingPage(self.page)

    def open_ui_elements(self) -> UiElementsPage:
        self._open_card("/practice-different-ui-elements")
        return UiElementsPage(self.page)

    def open_forgot_password(self) -> ForgotPasswordPage:
        self._open_card("/forget-password")
        return ForgotPasswordPage(self.page)

    def open_register(self) -> RegisterPage:
        self._open_card("/register")
        return RegisterPage(self.page)

    def open_contact_from_header(self) -> ContactPage:
        self.open_contact()
        return ContactPage(self.page)
