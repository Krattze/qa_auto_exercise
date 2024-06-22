from test_data.user import user, bad_creds


def test_get_user_detail(user_detail_endpoint, create_and_delete_user_after_test):
    user_detail_endpoint.get_user_details(user['email'])
    user_detail_endpoint.check_response_is_(200)
    user_detail_endpoint.check_json_code_is_(200)


def test_get_non_exist_user_detail(user_detail_endpoint, create_and_delete_user_after_test):
    user_detail_endpoint.get_user_details(bad_creds['email'])
    user_detail_endpoint.check_response_is_(200)
    user_detail_endpoint.check_json_code_is_(404)
    user_detail_endpoint.check_json_message_is_('Account not found with this email, try another email!')
