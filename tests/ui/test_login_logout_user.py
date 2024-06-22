from pages.home import HomePage
from test_data.user import user, bad_creds
import pytest


@pytest.mark.parametrize("credentials, expected_message", [
    (user, f"Logged in as {user['name']}"),
    (bad_creds, "Your email or password is incorrect!")
])
def test_login_user(page, create_and_delete_user_after_test, credentials, expected_message):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    signup_login_page = home_page.click_signup_login()
    signup_login_page.verify_text_is_visible('Login to your account')
    signup_login_page.enter_email_and_pass_to_login(credentials['email'], credentials['password'])
    home_page = signup_login_page.click_login_button()
    home_page.verify_text_is_visible(expected_message)
    if credentials == user:
        home_page.click_delete_account()
        home_page.verify_text_is_visible("ACCOUNT DELETED!")


def test_logout_user(page, create_and_delete_user_after_test):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    signup_login_page = home_page.click_signup_login()
    signup_login_page.verify_text_is_visible('Login to your account')
    signup_login_page.enter_email_and_pass_to_login(user['email'], user['password'])
    home_page = signup_login_page.click_login_button()
    home_page.verify_text_is_visible(f"Logged in as {user['name']}")
    home_page.click_logout()
    signup_login_page.verify_navigate_to_login_page()
