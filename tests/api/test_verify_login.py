from test_data.user import user, bad_creds


def test_post_verify_login(verify_login_endpoint, create_and_delete_user_after_test):
    verify_login_endpoint.verify_login(user)
    verify_login_endpoint.check_response_is_(200)
    verify_login_endpoint.check_json_code_is_(200)
    verify_login_endpoint.check_json_message_is_("User exists!")


def test_post_verify_login_wrong_cred(verify_login_endpoint, create_and_delete_user_after_test):
    verify_login_endpoint.verify_login(bad_creds)
    verify_login_endpoint.check_response_is_(200)
    verify_login_endpoint.check_json_code_is_(404)
    verify_login_endpoint.check_json_message_is_("User not found!")
