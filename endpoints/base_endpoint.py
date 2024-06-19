class Endpoint:
    response = None
    response_json = None

    def check_response_is_(self, code):
        assert self.response.status_code == code

    def check_json_code_is_(self, code):
        assert self.response_json['responseCode'] == code

    def check_json_message_is_(self, message):
        assert self.response_json['message'] == message
