"""Shared test setup.

You do not create the browser here. The pytest-playwright plugin does.

Every test can take an argument named `page`. That is a new browser tab.
The plugin closes it when the test finishes, pass or fail.

    def test_something(page):
        login = LoginPage(page)
        login.open()

Allure: pytest writes raw files into allure-results/.
That folder is not the report. Open the report with the Allure command:

    uv run pytest
    allure serve allure-results
"""

import sys
from pathlib import Path

import allure
import pytest

from config import BASE_URL


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """After a failed test, attach a screenshot to the Allure result.

    This runs before the browser closes, so the page is still available.
    A passing test does not need a picture.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    try:
        allure.attach(
            page.url,
            name="page url",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        # The browser may already be gone. Keep the original test failure.
        return


def pytest_sessionfinish(session, exitstatus):
    """A few facts shown on the Allure Overview page."""
    results = Path("allure-results")
    results.mkdir(exist_ok=True)
    results.joinpath("environment.properties").write_text(
        "\n".join(
            [
                "Framework=Playwright + pytest",
                "Browser=chromium",
                f"BaseURL={BASE_URL}",
                f"Python={sys.version.split()[0]}",
                "",
            ]
        )
    )
