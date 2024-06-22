from test_data.user import user


def test_create_account(account_endpoint, delete_user_before_test, delete_user_after_test):
    account_endpoint.create_account(user)
    account_endpoint.check_response_is_(200)
    account_endpoint.check_json_code_is_(201)
    account_endpoint.check_json_message_is_("User created!")


def test_delete_account(account_endpoint, create_test_user, delete_user_after_test):
    account_endpoint.delete_account(user["email"], user["password"])
    account_endpoint.check_response_is_(200)
    account_endpoint.check_json_code_is_(200)
    account_endpoint.check_json_message_is_("Account deleted!")

