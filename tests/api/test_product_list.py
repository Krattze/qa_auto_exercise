from test_data.test_products import new_product


def test_get_all_products(product_list_endpoint):
    product_list_endpoint.get_all_products()
    product_list_endpoint.check_response_is_(200)
    product_list_endpoint.check_json_code_is_(200)
    product_list_endpoint.check_json_contains_product_list()


# Как будто проверяем, что после добавления нового товара,
# сможем получить его
def test_all_products_contains_new(product_list_endpoint):
    product_list_endpoint.get_all_products()
    product_list_endpoint.check_response_is_(200)
    product_list_endpoint.check_json_code_is_(200)
    product_list_endpoint.check_json_contains_product_list()
    product_list_endpoint.check_product_list_contains_(new_product)


def test_post_all_products(product_list_endpoint):
    product_list_endpoint.post_all_products()
    product_list_endpoint.check_response_is_(200)
    product_list_endpoint.check_json_code_is_(405)
    product_list_endpoint.check_json_message_is_("This request method is not supported.")
