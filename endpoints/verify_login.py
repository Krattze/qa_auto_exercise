from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class VerifyLoginEndpoint(Endpoint):
    @allure.step("Проверить существование пользователя")
    def verify_login(self, creds):
        creds = {
            'email': f"{creds['email']}",
            'password': f"{creds['password']}"
        }
        with allure.step(f"POST запрос на verify_login endpoint с данными: {creds}"):
            self.response = requests.post(Urls.VERIFY_LOGIN_URL, data=creds)
            self.response_json = self.response.json()
