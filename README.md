# QA Practice test framework

A small UI test project for [qapractice.com](https://www.qapractice.com/).
It uses **Python**, **pytest**, **Playwright**, **Allure**, and **uv**.

The layout follows the Page Object Model and the KISS principle:
one class per screen, short methods, locators kept out of the tests.

## Layout

```
config.py                 shared URL and demo credentials
pages/                    one class per screen (the page objects)
tests/                    the tests themselves
tests/conftest.py         notes on the browser fixture
pyproject.toml            dependencies and pytest settings
```

A test should read like a user action:

```python
login = LoginPage(page)
login.open()
login.login(DEMO_EMAIL, DEMO_PASSWORD)
expect(login.success_message).to_contain_text("Login Successful")
```

The test does not know that the email field is `data-testid=login-email`.
That detail stays inside `pages/login_page.py`.

## Setup

Install [uv](https://docs.astral.sh/uv/) if you do not have it, then:

```bash
uv sync
uv run playwright install chromium
```

## Run

```bash
uv run pytest                  # all tests, no browser window
uv run pytest --headed         # watch the browser
uv run pytest tests/test_login.py
uv run pytest -k "empty"       # run tests whose name contains "empty"
```

## Allure report

pytest writes raw results to `allure-results/`.
The HTML report is a second step. Install the Allure command line once
([install guide](https://allurereport.org/docs/install/)):

```bash
brew install allure
```

Then:

```bash
uv run pytest
allure serve allure-results          # open the report in a browser
allure generate allure-results -o allure-report --clean
```

`allure serve` deletes its temporary copy when you stop it.
`allure generate` leaves a folder you can open later: `allure-report/index.html`.

A failed test attaches a screenshot and the page URL.
`@allure.feature` groups tests. `allure.step` is one line in the report.

## Add a new page

1. Copy `pages/login_page.py`.
2. Change the path and the locators. Prefer `get_by_test_id`.
3. Add a short method for the user action (`login`, `search`, `send`).
4. Add a test under `tests/` that calls that method and checks the result.

The demo login on the site is `user@premiumbank.com` / `Bank@123`.
Both values live in `config.py`.
