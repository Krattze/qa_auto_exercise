from pages.home import HomePage
import pytest


def test_subscription_in_home_page(page):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    home_page.scroll_to_bottom()
    home_page.verify_text_in_viewport("Subscription")
    home_page.enter_email_to_subscribe("test@mail.ru")
    home_page.click_on_subscribe_arrow()
    home_page.verify_text_is_visible("You have been successfully subscribed!")


