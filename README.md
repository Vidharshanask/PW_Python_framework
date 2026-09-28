# Playwright Python Test Automation Framework

[![Playwright Tests](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml)

A modular UI and API test automation framework built with **Python**, **Playwright**, and **pytest**. It uses the **Page Object Model (POM)**, fixture-based browser management, and continuous integration via **GitHub Actions**.

**Targets:** [SauceDemo](https://www.saucedemo.com/) (UI) and [ReqRes](https://reqres.in/) (REST API)

---

## Key Features

- **Page Object Model (POM):** UI locators and page interactions separated from test assertions (`LoginPage`, `InventoryPage`, `CheckoutPage`).
- **Fixture architecture:** Browser context and lifecycle managed in `conftest.py`, with setup and teardown isolated per test.
- **REST API testing:** Playwright's `APIRequestContext` for GET, POST and PUT requests, with status code and JSON payload assertions and no third-party HTTP client.
- **Data-driven tests:** `@pytest.mark.parametrize` for negative login and boundary cases.
- **HTML reporting with screenshots:** `pytest-html` report with base64 failure screenshots captured through a pytest hook wrapper.
- **CI/CD:** GitHub Actions runs headless on Ubuntu for push, pull request and manual dispatch, and archives the test report as an artifact.

---

## Project Structure

```
PW_Python_framework/
├── .github/
│   └── workflows/
│       └── playwright.yml     # GitHub Actions CI workflow
├── pages/
│   ├── __init__.py
│   ├── login_page.py          # Login interactions & locators
│   ├── inventory_page.py      # Catalog & cart actions
│   └── checkout_page.py       # Checkout form & completion
├── conftest.py                # Fixtures, browser lifecycle, failure hook
├── test_login.py              # Positive & parameterized negative login tests
├── test_checkout.py           # End-to-end purchase flow
├── test_api.py                # REST API tests
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

```bash
git clone https://github.com/Vidharshanask/PW_Python_framework.git
cd PW_Python_framework

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

---

## Running Tests

```bash
# Full suite (headless by default)
pytest -v

# Headed mode for local debugging
# PowerShell:
$env:HEADED=1; pytest -v
Remove-Item Env:HEADED          # switch back to headless

# macOS / Linux:
HEADED=1 pytest -v

# Individual modules
pytest test_login.py -v
pytest test_checkout.py -v
pytest test_api.py -v

# Standalone HTML report
pytest -v --html=report.html --self-contained-html
```

---

## CI/CD Pipeline (GitHub Actions)

The workflow runs on:
- **Push** to `main` or `master`
- **Pull requests** targeting `main` or `master`
- **Manual dispatch** (`workflow_dispatch`) from the Actions tab

**Pipeline details:**
- **Runner:** `ubuntu-latest`
- **Execution:** headless Chromium with OS dependencies (`playwright install chromium --with-deps`)
- **Artifacts:** `report.html` is uploaded on every run, even when tests fail (`if: always()`), and retained for 14 days. Download it from the run page in the **Actions** tab.