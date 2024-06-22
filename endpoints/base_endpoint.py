import allure


class Endpoint:
    response = None
    response_json = None

    @allure.step("Проверить, что код ответа: {code}")
    def check_response_is_(self, code):
        assert self.response.status_code == code

    @allure.step("Проверить, что код ответа в JSON: {code}")
    def check_json_code_is_(self, code):
        assert self.response_json['responseCode'] == code

    @allure.step("Проверить, что сообщение в JSON: {message}")
    def check_json_message_is_(self, message):
        assert self.response_json['message'] == message
