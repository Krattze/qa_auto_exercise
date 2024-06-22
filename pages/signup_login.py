from pages.base_page import BasePage
from playwright.sync_api import expect


SIGNUP_NAME = 'input[data-qa="signup-name"]'
SIGNUP_EMAIL = 'input[data-qa="signup-email"]'
SIGNUP_BUTTON = 'button[data-qa="signup-button"]'
LOGIN_EMAIL = 'input[data-qa="login-email"]'
LOGIN_PASS = 'input[data-qa="login-password"]'
LOGIN_BUTTON = 'button[data-qa="login-button"]'
PAGE_TITLE = 'Automation Exercise - Signup / Login'

class SignupLoginPage(BasePage):
    #url = 'https://www.automationexercise.com/login'

    def enter_name_and_email_to_signup(self, name, email):
        self.page.locator(SIGNUP_NAME).fill(name)
        self.page.locator(SIGNUP_EMAIL).fill(email)

    def click_signup_button(self):
        self.page.locator(SIGNUP_BUTTON).click()
        from pages.signup import SignupPage
        return SignupPage(self.page)

    def enter_email_and_pass_to_login(self, email, password):
        self.page.locator(LOGIN_EMAIL).fill(email)
        self.page.locator(LOGIN_PASS).fill(password)

    def click_login_button(self):
        self.page.locator(LOGIN_BUTTON).click()
        from pages.home import HomePage
        return HomePage(self.page)

    def verify_navigate_to_login_page(self):
        expect(self.page).to_have_title(PAGE_TITLE)



