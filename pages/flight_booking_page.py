"""Flight booking wizard: /flight-booking-scenarios

Step 1 is a search form (cities are <select> elements).
Later steps are results, passengers, then payment.
This class only wraps step 1 plus the final success banner.
Add the later steps the same way when you write those tests.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class FlightBookingPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/flight-booking-scenarios")
        self.from_city = page.get_by_test_id("flight-from")
        self.to_city = page.get_by_test_id("flight-to")
        self.departure_date = page.get_by_test_id("flight-departure-date")
        self.return_date = page.get_by_test_id("flight-return-date")
        self.passengers = page.get_by_test_id("flight-passengers")
        self.travel_class = page.get_by_test_id("flight-class")
        self.one_way = page.get_by_test_id("flight-one-way")
        self.search_button = page.get_by_test_id("flight-search")
        self.success_message = page.get_by_test_id("flight-booking-success")
        self.ready = self.from_city

    def search_one_way(self, origin: str, destination: str, departure: str) -> None:
        """departure is a date input value, for example "2026-11-01"."""
        self.one_way.check()
        self.from_city.select_option(origin)
        self.to_city.select_option(destination)
        self.departure_date.fill(departure)
        self.search_button.click()
