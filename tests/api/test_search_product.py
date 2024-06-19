from endpoints.search_product import SearchProductEndpoint


# TODO: Parametrize
def test_post_search_product():
    search = SearchProductEndpoint()
    search.search_product("TShirt")
    search.check_response_is_(200)
    search.check_json_code_is_(200)


def test_post_search_product_without_parametr():
    search = SearchProductEndpoint()
    search.search_product()
    search.check_response_is_(200)
    search.check_json_code_is_(400)
    search.check_json_message_is_("Bad request, search_product parameter is missing in POST request.")
