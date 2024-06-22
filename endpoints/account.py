from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class AccountEndpoint(Endpoint):

    @allure.step("Создание аккаунта")
    def create_account(self, user):
        with allure.step(f"POST запрос на create_account endpoint с данными: {user}"):
            self.response = requests.post(Urls.CREATE_ACCOUNT_URL, data=user)
            self.response_json = self.response.json()

    @allure.step("Удаление аккаунта")
    def delete_account(self, email, password):
        creds = {
            'email': f"{email}",
            'password': f"{password}"
        }
        with allure.step(f"DELETE запрос на delete_account endpoint с данными: {creds}"):
            self.response = requests.delete(Urls.DELETE_ACCOUNT_URL, data=creds)
            self.response_json = self.response.json()
