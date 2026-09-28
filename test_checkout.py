from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(page):
    # 1. Initialize Page Objects using the fixture
    login_pg = LoginPage(page)
    inventory_pg = InventoryPage(page)
    checkout_pg = CheckoutPage(page)

    # 2. Login
    login_pg.navigate()
    login_pg.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 3. Add to cart
    inventory_pg.add_bike_light_to_cart()
    expect(inventory_pg.cart_badge).to_have_text("1")

    # 4. View Cart
    inventory_pg.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(checkout_pg.cart_item_name).to_have_text("Sauce Labs Bike Light")

    # 5. Fill Checkout Information
    checkout_pg.proceed_to_checkout()
    checkout_pg.fill_checkout_info("vid", "sk", "560066")

    # 6. Overview & Finish
    expect(checkout_pg.overview_title).to_have_text("Checkout: Overview")
    checkout_pg.finish_order()

    # 7. Order Confirmation
    expect(checkout_pg.complete_header).to_have_text("Thank you for your order!")