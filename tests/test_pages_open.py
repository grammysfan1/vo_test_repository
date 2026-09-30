"""Smoke test: each page object can open its screen.

A smoke test does not check business rules. It only checks
"does the page load, and is the main control there?"
If this fails, the locator or the URL is wrong.
"""

import allure
import pytest
from playwright.sync_api import expect

from pages.contact_page import ContactPage
from pages.flight_booking_page import FlightBookingPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.forms_page import FormsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.practice_sites_page import PracticeSitesPage
from pages.register_page import RegisterPage
from pages.shop_page import ShopPage
from pages.ui_elements_page import UiElementsPage

# (page class, name of the attribute we expect to see)
PAGES = [
    (HomePage, "ready"),
    (PracticeSitesPage, "ready"),
    (LoginPage, "ready"),
    (RegisterPage, "ready"),
    (ForgotPasswordPage, "ready"),
    (FormsPage, "ready"),
    (ShopPage, "ready"),
    (FlightBookingPage, "ready"),
    (UiElementsPage, "ready"),
    (ContactPage, "ready"),
]


@allure.feature("Smoke")
@allure.story("Pages open")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "page_class, ready_name",
    PAGES,
    ids=[page_class.__name__ for page_class, _ in PAGES],
)
def test_page_opens(page, page_class, ready_name):
    # The title changes per page, so it is set here instead of with a decorator.
    allure.dynamic.title(f"{page_class.__name__} opens")
    screen = page_class(page)

    with allure.step(f"Open {page_class.__name__}"):
        screen.open()

    with allure.step("The main control is visible"):
        expect(getattr(screen, ready_name)).to_be_visible()
