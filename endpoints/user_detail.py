from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class UserDetailsEndpoint(Endpoint):

    @allure.step("Получить информацию о пользователе")
    def get_user_details(self, email=None):
        data = {'email': email} if email else {}
        with allure.step(f"GET запрос на user_details endpoint с параметрами: {data}"):
            self.response = requests.get(Urls.USER_DETAIL_URL, params=data)
            self.response_json = self.response.json()
