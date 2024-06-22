from pages.base_page import BasePage

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

    def fill_details(self, password, firstname, lastname, address, zipcode, state, city, mobile_number):
        self.page.locator(RADIO_BUTTON).check()
        self.page.locator(PASSWORD).fill(password)
        self.page.locator(SELECT_DAYS).select_option("1")
        self.page.locator(SELECT_MONTH).select_option("1")
        self.page.locator(SELECT_YEAR).select_option("2000")
        self.page.locator(CHECKBOX_NEWSLETTER).check()
        self.page.locator(CHECKBOX_OFFERS).check()
        self.page.locator(FIRST_NAME).fill(firstname)
        self.page.locator(LAST_NAME).fill(lastname)
        self.page.locator(ADDRESS).fill(address)
        self.page.locator(STATE).fill(state)
        self.page.locator(CITY).fill(city)
        self.page.locator(ZIPCODE).fill(zipcode)
        self.page.locator(MOBILE).fill(mobile_number)

    def click_create_account_button(self):
        self.page.locator(CREATE_ACC_BUTTON).click()

    def click_continue_button(self):
        self.page.locator(CONTINUE_BUTTON).click()
        from pages.home import HomePage
        return HomePage(self.page)
