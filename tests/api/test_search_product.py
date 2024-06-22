import pytest


@pytest.mark.parametrize("product_to_search, should_have_products", [
    ("tshirt", True),
    ("jeans", True),
    ("shoes", False)
])
def test_post_search_product(search_product_endpoint,product_to_search,should_have_products):
    search_product_endpoint.search_product(product_to_search)
    search_product_endpoint.check_response_is_(200)
    search_product_endpoint.check_json_code_is_(200)
    search_product_endpoint.check_product_category_equal_search_name(product_to_search, should_have_products)


def test_post_search_product_without_parametr(search_product_endpoint):
    search_product_endpoint.search_product()
    search_product_endpoint.check_response_is_(200)
    search_product_endpoint.check_json_code_is_(400)
    search_product_endpoint.check_json_message_is_("Bad request, search_product parameter is missing in POST request.")
