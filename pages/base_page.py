import allure
from playwright.sync_api import Page, expect


class BasePage:
    url = None

    def __init__(self, page:Page):
        self.page = page

    def open(self):
        with allure.step(f"Открыть страницу {self.url}"):
            if self.url:
                self.page.goto(self.url)

    @allure.step("Проверить, что текст '{text}' виден на странице")
    def verify_text_is_visible(self, text):
        expect(self.page.get_by_text(text)).to_be_visible()

    @allure.step("Прокрутить страницу до конца вниз")
    def scroll_to_bottom(self):
        self.page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

    @allure.step("Прокрутить страницу до конца вверх")
    def scroll_to_top(self):
        self.page.evaluate('window.scrollTo(0, 0)')

    @allure.step("Проверить, что текст '{text}' находится в видимой области")
    def verify_text_in_viewport(self, text):
        expect(self.page.get_by_text(text).first).to_be_in_viewport()
