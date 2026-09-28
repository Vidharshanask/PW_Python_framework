import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page  # Hands the active page over to your test function

        # Cleanup runs automatically after each test completes
        context.close()
        browser.close()