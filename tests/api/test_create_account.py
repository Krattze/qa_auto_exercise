from endpoints.account import AccountEndpoint

user = {
    'name': "Test",
    'email': "test12345@mail.ru",
    'password': "123",
    'firstname': "test",
    'lastname': "test",
    'company': "test",
    'address1': "test",
    'country': "test",
    'zipcode': "test",
    'state': "test",
    'city': "test",
    'mobile_number': "test"
}

user_creds = {
    'email': "test12345@mail.ru",
    'password': "123"
}


def test_create_account():
    new_account = AccountEndpoint()
    new_account.create_account(user)
    new_account.check_response_is_(200)
    new_account.check_json_code_is_(201)
    new_account.check_json_message_is_("User created!")


def test_delete_account():
    account = AccountEndpoint()
    account.delete_account(user_creds)
    account.check_response_is_(200)
    account.check_json_code_is_(200)
    account.check_json_message_is_("Account deleted!")

