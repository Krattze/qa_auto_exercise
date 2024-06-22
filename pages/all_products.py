import allure
from pages.base_page import BasePage
from playwright.sync_api import expect

PRODUCT_CARD = '.productinfo'
PRODUCT_IMG = 'img'
PRODUCT_PRICE = 'h2'
PRODUCT_NAME = 'p'
FIRST_PRODUCT = 'a[href="/product_details/1"]'


class AllProductsPage(BasePage):

    @allure.step('Проверка отображения списка продуктов')
    def check_products_list_is_visible(self):
        products = self.page.locator(PRODUCT_CARD)
        count = products.count()
        with allure.step(f'Обнаружено продуктов: {count}'):
            for i in range(count):
                product = products.nth(i)
                with allure.step(f'Проверка продукта {i + 1}'):
                    with allure.step('Проверка изображения продукта'):
                        expect(product.locator(PRODUCT_IMG)).to_be_visible()
                    with allure.step('Проверка цены продукта'):
                        expect(product.locator(PRODUCT_PRICE)).to_be_visible()
                    with allure.step('Проверка названия продукта'):
                        expect(product.locator(PRODUCT_NAME)).to_be_visible()

    @allure.step('Кликаем на первый продукт в списке')
    def click_on_view_product_first(self):
        self.page.locator(FIRST_PRODUCT).click()
        from pages.product_details import ProductDetails
        allure.attach(self.page.screenshot(), name='First_Product_Clicked', attachment_type=allure.attachment_type.PNG)
        return ProductDetails(self.page)
