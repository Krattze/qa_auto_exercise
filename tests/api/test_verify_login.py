from endpoints.verify_login import VerifyLoginEndpoint

creds = {
    'email': "test1234@mail.ru",
    'password': "123"
}

bad_creds = {
    'email': "test1234@mail.ru",
    'password': "1232131"
}


def test_post_verify_login():
    login = VerifyLoginEndpoint()
    login.verify_login(creds)
    login.check_response_is_(200)
    login.check_json_code_is_(200)
    login.check_json_message_is_("User exists!")


def test_post_verify_login_bad_cred():
    login = VerifyLoginEndpoint()
    login.verify_login(bad_creds)
    login.check_response_is_(200)
    login.check_json_code_is_(404)
    login.check_json_message_is_("User not found!")
