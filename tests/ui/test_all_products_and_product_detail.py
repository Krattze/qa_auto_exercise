from pages.home import HomePage


def test_all_products_and_product_details(page):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_visible_success()
    products_page = home_page.click_products()
    products_page.verify_text_is_visible("ALL PRODUCTS")
    products_page.check_products_list_is_visible()
    product_details_page = products_page.click_on_view_product_first()
    product_details_page.check_product_details_is_visible()
