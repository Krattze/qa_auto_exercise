from endpoints.user_detail import UserDetailsEndpoint


def test_get_user_detail():
    user_detail = UserDetailsEndpoint()
    email = "test1234@mail.ru"
    user_detail.get_user_details(email)
    user_detail.check_response_is_(200)
    user_detail.check_json_code_is_(200)
