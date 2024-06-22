
def test_get_all_brands(brands_list_endpoint):
    brands_list_endpoint.get_all_brands()
    brands_list_endpoint.check_response_is_(200)
    brands_list_endpoint.check_json_code_is_(200)
    brands_list_endpoint.check_json_contains_brands_list()


def test_put_all_brands(brands_list_endpoint):
    brands_list_endpoint.put_all_brands()
    brands_list_endpoint.check_response_is_(200)
    brands_list_endpoint.check_json_code_is_(405)
    brands_list_endpoint.check_json_message_is_("This request method is not supported.")
