from pages.base_page import BasePage
import allure

RADIO_BUTTON = "#id_gender1"
PASSWORD = "#password"
SELECT_DAYS = "#days"
SELECT_MONTH = "#months"
SELECT_YEAR = "#years"
CHECKBOX_NEWSLETTER = "#newsletter"
CHECKBOX_OFFERS = "#optin"
FIRST_NAME = "#first_name"
LAST_NAME = "#last_name"
ADDRESS = "#address1"
STATE = "#state"
CITY = "#city"
ZIPCODE = "#zipcode"
MOBILE = "#mobile_number"
CREATE_ACC_BUTTON = 'button[data-qa="create-account"]'
CONTINUE_BUTTON = 'a[data-qa="continue-button"]'


class SignupPage(BasePage):

    @allure.step("Заполнить детали регистрации")
    def fill_details(self, password, firstname, lastname, address, zipcode, state, city, mobile_number):
        with allure.step("Выбор пола"):
            self.page.locator(RADIO_BUTTON).check()
        with allure.step("Заполнение пароля"):
            self.page.locator(PASSWORD).fill(password)
        with allure.step("Выбор дня рождения"):
            self.page.locator(SELECT_DAYS).select_option("1")
        with allure.step("Выбор месяца рождения"):
            self.page.locator(SELECT_MONTH).select_option("1")
        with allure.step("Выбор года рождения"):
            self.page.locator(SELECT_YEAR).select_option("2000")
        with allure.step("Отметка чекбокса для подписки на новости"):
            self.page.locator(CHECKBOX_NEWSLETTER).check()
        with allure.step("Отметка чекбокса для специальных предложений"):
            self.page.locator(CHECKBOX_OFFERS).check()
        with allure.step("Заполнение имени"):
            self.page.locator(FIRST_NAME).fill(firstname)
        with allure.step("Заполнение фамилии"):
            self.page.locator(LAST_NAME).fill(lastname)
        with allure.step("Заполнение адреса"):
            self.page.locator(ADDRESS).fill(address)
        with allure.step("Заполнение штата"):
            self.page.locator(STATE).fill(state)
        with allure.step("Заполнение города"):
            self.page.locator(CITY).fill(city)
        with allure.step("Заполнение почтового индекса"):
            self.page.locator(ZIPCODE).fill(zipcode)
        with allure.step("Заполнение мобильного номера"):
            self.page.locator(MOBILE).fill(mobile_number)

    @allure.step("Нажать на кнопку создания аккаунта")
    def click_create_account_button(self):
        self.page.locator(CREATE_ACC_BUTTON).click()

    @allure.step("Нажать на кнопку продолжения")
    def click_continue_button(self):
        self.page.locator(CONTINUE_BUTTON).click()
        from pages.home import HomePage
        return HomePage(self.page)
