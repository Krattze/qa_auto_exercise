import requests
from endpoints.product_list import ProductListEndpoint

new_product = {
    "id": 43,
    "name": "GRAPHIC DESIGN MEN T SHIRT - BLUE",
    "price": "Rs. 1389",
    "brand": "Mast & Harbour",
    "category": {
        "usertype": {
            "usertype": "Men"
        },
        "category": "Tshirts"
    }
}

def test_get_all_products():
    product_list = ProductListEndpoint()
    product_list.get_all_products()
    product_list.check_response_is_(200)
    product_list.check_json_code_is_(200)
    product_list.check_json_contains_product_list()


def test_all_products_contains_new():
    product_list = ProductListEndpoint()
    product_list.get_all_products()
    product_list.check_response_is_(200)
    product_list.check_json_code_is_(200)
    product_list.check_json_contains_product_list()
    # Как будто проверяем, что после добавления нового товара,
    # сможем получить его
    product_list.check_product_list_contains_(new_product)


def test_post_all_products():
    product_list = ProductListEndpoint()
    product_list.post_all_products()
    product_list.check_response_is_(200)
    product_list.check_json_code_is_(405)
    product_list.check_json_message_is_("This request method is not supported.")












