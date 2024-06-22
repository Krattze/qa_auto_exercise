from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class BrandsListEndpoint(Endpoint):

    @allure.step("Полкчить список с брендами")
    def get_all_brands(self):
        with allure.step("GET запрос на all_brands endpoint"):
            self.response = requests.get(Urls.BRAND_LIST_URL)
            self.response_json = self.response.json()

    @allure.step("Проверить метод PUT")
    def put_all_brands(self):
        with allure.step("PUT запрос на all_brands endpoint"):
            self.response = requests.put(Urls.PRODUCT_LIST_URL)
            self.response_json = self.response.json()

    @allure.step("Проверить наличие списка брендов в JSON ответе")
    def check_json_contains_brands_list(self):
        assert "brands" in self.response_json
