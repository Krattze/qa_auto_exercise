from endpoints.brand_list import BrandsListEndpoint


def test_get_all_brands():
    brands_list = BrandsListEndpoint()
    brands_list.get_all_brands()
    brands_list.check_response_is_(200)
    brands_list.check_json_code_is_(200)
    brands_list.check_json_contains_brands_list()


def test_put_all_brands():
    brands_list = BrandsListEndpoint()
    brands_list.put_all_brands()
    brands_list.check_response_is_(200)
    brands_list.check_json_code_is_(405)
    brands_list.check_json_message_is_("This request method is not supported.")
