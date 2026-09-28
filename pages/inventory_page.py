class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_bike_light_btn = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_bike_light_to_cart(self):
        self.add_bike_light_btn.click()

    def go_to_cart(self):
        self.cart_link.click()