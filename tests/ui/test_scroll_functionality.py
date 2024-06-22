from pages.home import HomePage
import pytest


@pytest.mark.parametrize("scroll_up_using_arrow", [True, False])
def test_scrolling(page, scroll_up_using_arrow):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    home_page.scroll_to_bottom()
    home_page.verify_text_in_viewport("Subscription")
    if scroll_up_using_arrow:
        home_page.click_on_scrollup_arrow()
    else:
        home_page.scroll_to_top()
    home_page.verify_text_in_viewport("Full-Fledged practice website for Automation Engineers")
