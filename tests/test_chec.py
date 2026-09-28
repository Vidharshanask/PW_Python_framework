from playwright.sync_api import sync_playwright,expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()

    page.get_by_text("Checkout").click()
    page.get_by_placeholder("First Name").fill("vid")
    page.get_by_placeholder("Last Name").fill("sk")
    page.get_by_placeholder("ZIP/Postal Code").fill("560066")
    page.get_by_role("button", name="Continue").click()

    expect(page.get_by_text("Checkout: Overview")).to_be_visible()
    page.get_by_role("button", name="Finish").click()

    page.wait_for_timeout(3000)
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()

    browser.close()