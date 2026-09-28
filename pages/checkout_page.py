class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.cart_item_name = page.locator('[data-test="inventory-item-name"]').first
        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_input = page.get_by_placeholder("ZIP/Postal Code")
        self.continue_btn = page.locator('[data-test="continue"]')
        self.overview_title = page.locator('[data-test="title"]')
        self.finish_btn = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')

    def proceed_to_checkout(self):
        self.checkout_btn.click()

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_input.fill(zip_code)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()