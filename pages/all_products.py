from pages.base_page import BasePage
from playwright.sync_api import expect

PRODUCT_CARD = '.productinfo'
PRODUCT_IMG = 'img'
PRODUCT_PRICE = 'h2'
PRODUCT_NAME = 'p'
FIRST_PRODUCT = 'a[href="/product_details/1"]'


class AllProductsPage(BasePage):

    def check_products_list_is_visible(self):
        products = self.page.locator(PRODUCT_CARD)
        count = products.count()
        for i in range(count):
            product = products.nth(i)
            expect(product.locator(PRODUCT_IMG)).to_be_visible()
            expect(product.locator(PRODUCT_PRICE)).to_be_visible()
            expect(product.locator(PRODUCT_NAME)).to_be_visible()

    def click_on_view_product_first(self):
        self.page.locator(FIRST_PRODUCT).click()
        from pages.product_details import ProductDetails
        return ProductDetails(self.page)

