from pages.home import HomePage
from test_data.user import user


def test_register_user(page, delete_user_before_test, delete_user_after_test):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    signup_login_page = home_page.click_signup_login()
    signup_login_page.verify_text_is_visible("New User Signup!")
    signup_login_page.enter_name_and_email_to_signup(user["name"], user["email"])
    signup_page = signup_login_page.click_signup_button()
    signup_page.verify_text_is_visible("ENTER ACCOUNT INFORMATION")
    signup_page.fill_details(user["password"], user["firstname"], user["lastname"], user["address1"],
                             user["zipcode"], user["state"], user["city"], user["mobile_number"])
    signup_page.click_create_account_button()
    signup_page.verify_text_is_visible("ACCOUNT CREATED!")
    home_page = signup_page.click_continue_button()
    home_page.verify_text_is_visible(f"Logged in as {user['name']}")


def test_register_user_with_existing_email(page, create_and_delete_user_after_test):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    signup_login_page = home_page.click_signup_login()
    signup_login_page.verify_text_is_visible("New User Signup!")
    signup_login_page.enter_name_and_email_to_signup(user["name"], user["email"])
    signup_login_page.click_signup_button()
    signup_login_page.verify_text_is_visible("Email Address already exist!")
