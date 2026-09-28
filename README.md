# Playwright Python Test Automation Framework
[![Playwright Tests](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/Vidharshanask/PW_Python_framework/actions/workflows/playwright.yml)

A modular, maintainable UI and API test automation framework built using **Python**, **Playwright**, and **pytest**. This project demonstrates industry-standard automation patterns, including the **Page Object Model (POM)** for UI workflows on SauceDemo and automated REST API validations against ReqRes using Playwright's native network client.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.10+
* **Framework / Runner:** pytest
* **Automation Library:** Playwright (Python Synchronous API)
* **Design Pattern:** Page Object Model (POM)
* **Target Applications:**
  * **UI Application:** [SauceDemo](https://www.saucedemo.com/)
  * **API Service:** [ReqRes](https://reqres.in/)

---

## 📁 Project Directory Structure

project_pw/
│
├── pages/                       # Page Object Model (POM) classes
│   ├── __init__.py              # Package marker
│   ├── login_page.py            # Locators & actions for SauceDemo Login
│   ├── inventory_page.py        # Catalog interactions and add-to-cart flows
│   └── checkout_page.py         # Multi-step checkout form & order completion
│
├── conftest.py                  # Pytest fixture managing browser lifecycle
├── test_login.py                # Positive & parameterized negative login tests
├── test_checkout.py             # Complete end-to-end checkout workflow test
├── test_api.py                  # REST API tests (GET, POST, PUT)
├── requirements.txt             # Project dependencies
├── pytest.ini                   # Pytest configuration & path resolution
├── .gitignore                   # Ignore cache, environment, and report files
└── README.md                    # Project documentation

---

## 🚀 Key Framework Highlights
* Page Object Model (POM): Encapsulates web elements and page actions in dedicated classes (LoginPage, InventoryPage, CheckoutPage), eliminating hardcoded selectors across test files.

* Centralized Browser Fixtures (conftest.py): Uses @pytest.fixture(scope="function") to manage browser launching, context isolation, and automatic teardown (yield) via pytest dependency injection.

* Data-Driven Parameterization: Utilizes @pytest.mark.parametrize in test_login.py to validate multiple boundary conditions (locked-out user, wrong password, missing fields) within a single test definition.

* Integrated REST API Automation: Uses Playwright's native APIRequestContext in test_api.py to send GET, POST, and PUT requests, asserting HTTP status codes and JSON payloads without extra HTTP libraries.

---

## ⚙️ Installation & Environment Setup
1. Clone the Repository
git clone https://github.com/Vidharshanask/Playwright_skv.git
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
Run the full test suite (UI + API):
pytest -v

Run only UI tests:
pytest test_login.py test_checkout.py -v

Run only parameterized login tests:
pytest test_login.py -v

Run only API tests:
pytest test_api.py -v

Run tests in headless mode (CI-friendly):
pytest -v --headed=false

---

### Push It to GitHub

Once you save the file, execute these commands in your Windows terminal:

```cmd
git add README.md
git commit -m "docs: clean up formatting, code fences, and section dividers in README"
git push