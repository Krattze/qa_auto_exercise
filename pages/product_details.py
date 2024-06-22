from pages.base_page import BasePage
from playwright.sync_api import expect

PRODUCT_NAME = '.product-information h2'
PRODUCT_CATEGORY = '.product-information p:nth-of-type(1)'
PRODUCT_PRICE = '.product-information span span'
PRODUCT_AVAILABILITY = '.product-information p:nth-of-type(2)'
PRODUCT_CONDITION = '.product-information p:nth-of-type(3)'
PRODUCT_BRAND = '.product-information p:nth-of-type(4)'


class ProductDetails(BasePage):

    def check_product_details_is_visible(self):
        expect(self.page.locator(PRODUCT_NAME)).to_be_visible()
        expect(self.page.locator(PRODUCT_CATEGORY)).to_be_visible()
        expect(self.page.locator(PRODUCT_PRICE)).to_be_visible()
        expect(self.page.locator(PRODUCT_AVAILABILITY)).to_be_visible()
        expect(self.page.locator(PRODUCT_CONDITION)).to_be_visible()
        expect(self.page.locator(PRODUCT_BRAND)).to_be_visible()