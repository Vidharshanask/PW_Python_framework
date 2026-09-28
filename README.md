# Playwright Python Test Automation Framework

[![Playwright Tests](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml)

A modular, production-ready UI and API test automation framework built with **Python**, **Playwright**, and **pytest**. Designed around the **Page Object Model (POM)** pattern, centralized fixture-based browser management, and continuous integration via **GitHub Actions**.

Target Application: [SauceDemo](https://www.saucedemo.com/) (UI) & [ReqRes](https://reqres.in/) (REST API)

---

## Key Features

- **Page Object Model (POM):** Decoupled UI element locators and page interactions from test assertions across modular classes (`LoginPage`, `InventoryPage`, `CheckoutPage`).
- **Centralized Fixture Architecture:** Managed browser context and lifecycle in `conftest.py` with automated setup/teardown isolation per test.
- **REST API Validation:** Native API test suite utilizing Playwright's `APIRequestContext` for request dispatching, schema/payload validation, and status assertions without third-party HTTP clients.
- **Data-Driven Parameterization:** Leveraged `@pytest.mark.parametrize` for negative login validation and boundary checks.
- **Automated HTML Reporting with Screenshots:** Integrated `pytest-html` with dynamic base64 screenshot capture on test failures via pytest hook wrappers.
- **Continuous Integration (CI/CD):** Automated workflow using GitHub Actions running headlessly on Ubuntu runners across push, pull request, and manual dispatch events, with automated test report artifact archiving.

---

## Framework Architecture

PW_Python_framework/
├── .github/
│   └── workflows/
│       └── playwright.yml     # GitHub Actions CI workflow definition
├── pages/
│   ├── __init__.py
│   ├── login_page.py          # POM: Authentication interactions & locators
│   ├── inventory_page.py      # POM: Catalog filtering & cart manipulation
│   └── checkout_page.py       # POM: Form handling & checkout completion
├── conftest.py                # Fixtures, browser lifecycle & failure reporting hooks
├── test_login.py              # Positive & parameterized negative login tests
├── test_checkout.py           # End-to-end purchasing workflow tests
├── test_api.py                # REST API test suite via Playwright request context
├── requirements.txt           # Framework dependencies
├── .gitignore                 # Artifact & cache exclusion rules
└── README.md                  # Project documentation & CI status

---

## 🚀 Key Framework Highlights
* Page Object Model (POM): Encapsulates web elements and page actions in dedicated classes (LoginPage, InventoryPage, CheckoutPage), eliminating hardcoded selectors across test files.

* Centralized Browser Fixtures (conftest.py): Uses @pytest.fixture(scope="function") to manage browser launching, context isolation, and automatic teardown (yield) via pytest dependency injection.

* Data-Driven Parameterization: Utilizes @pytest.mark.parametrize in test_login.py to validate multiple boundary conditions (locked-out user, wrong password, missing fields) within a single test definition.

* Integrated REST API Automation: Uses Playwright's native APIRequestContext in test_api.py to send GET, POST, and PUT requests, asserting HTTP status codes and JSON payloads without extra HTTP libraries.

---

## ⚙️ Installation & Environment Setup
1. Clone the Repository
git clone https://github.com/Vidharshanask/PW_Python_framework
cd Playwright_skv

2. Create and Activate Virtual Environment
# Windows (Command Prompt / PowerShell):
python -m venv venv
venv\Scripts\activate

# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Install Playwright Browser Binaries
playwright install chromium

---

## 🧪 Test Execution Commands
Run the Full Test Suite (Headless Default)
pytest -v
Run Tests in Headed Mode (Local Debugging)
pytest -v --headed

Run a Specific Test Module
# UI Login tests
pytest test_login.py -v

# UI Checkout flow
pytest test_checkout.py -v

# REST API tests
pytest test_api.py -v

Generate Standalone HTML Test Report
pytest -v --html=report.html --self-contained-html

---

### Step to Apply & Push the Fix

Run these commands in your project root terminal:

```cmd
git add README.md
git commit -m "docs: overhaul README to align directory structure, clean commands, and showcase CI"
git push origin main