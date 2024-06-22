from pages.base_page import BasePage
from playwright.sync_api import expect
import allure

SIGNUP_LOGIN = 'a[href="/login"]'
LOGO = ".logo"
DELETE_ACC = 'a[href="/delete_account"]'
LOGOUT = 'a[href="/logout"]'
PRODUCTS = 'a[href="/products"]'
SCROLL_UP_ARROW = "#scrollUp"
SUBSCRIBE_INPUT = "#susbscribe_email"
SUBSCRIBE_ARROW = "#subscribe"


class HomePage(BasePage):
    url = 'http://automationexercise.com'

    @allure.step('Проверка, что страница загружена успешно')
    def verify_page_visible_success(self):
        expect(self.page.locator(LOGO)).to_be_visible()

    @allure.step('Переход на страницу регистрации/входа')
    def click_signup_login(self):
        self.page.locator(SIGNUP_LOGIN).click()
        from pages.signup_login import SignupLoginPage
        return SignupLoginPage(self.page)

    @allure.step('Нажать на DELETE ACCOUNT')
    def click_delete_account(self):
        self.page.locator(DELETE_ACC).click()

    @allure.step('Нажать на logout')
    def click_logout(self):
        self.page.locator(LOGOUT).click()

    @allure.step('Переход на страницу продуктов')
    def click_products(self):
        self.page.locator(PRODUCTS).click()
        from pages.all_products import AllProductsPage
        return AllProductsPage(self.page)

    @allure.step('Нажать на стрелку прокрутки вверх')
    def click_on_scrollup_arrow(self):
        self.page.locator(SCROLL_UP_ARROW).click()

    @allure.step('Ввод email для подписки')
    def enter_email_to_subscribe(self, email):
        self.page.locator(SUBSCRIBE_INPUT).fill(email)

    @allure.step('Нажать на стрелку подписки')
    def click_on_subscribe_arrow(self):
        self.page.locator(SUBSCRIBE_ARROW).click()
