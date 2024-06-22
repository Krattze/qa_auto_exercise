from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class ProductListEndpoint(Endpoint):
    @allure.step("Получить список всех продуктов")
    def get_all_products(self):
        with allure.step(f"Выполнить GET запрос на all_products endpoint"):
            self.response = requests.get(Urls.PRODUCT_LIST_URL)
            self.response_json = self.response.json()

    @allure.step("Проверить метод POST")
    def post_all_products(self):
        with allure.step(f"Выполнить POST запрос на all_products endpoint"):
            self.response = requests.post(Urls.PRODUCT_LIST_URL)
            self.response_json = self.response.json()

    @allure.step("Проверить наличие списка продуктов в JSON ответе")
    def check_json_contains_product_list(self):
        assert "products" in self.response_json

    @allure.step("Проверить наличие продукта в списке продуктов")
    def check_product_list_contains_(self, product):
        products = self.response_json["products"]
        product = next((p for p in products if p['id'] == product['id']), None)
        with allure.step(f"Проверить, что продукт с id={product['id']} найден в списке"):
            assert product is not None
        with allure.step("Проверить, что название продукта соответствует ожидаемому"):
            assert product['name'] == product['name']
        with allure.step("Проверить, что цена продукта соответствует ожидаемой"):
            assert product['price'] == product['price']
        with allure.step("Проверить, что бренд продукта соответствует ожидаемому"):
            assert product['brand'] == product['brand']
        with allure.step("Проверить, что тип пользователя категории продукта соответствует ожидаемому"):
            assert product['category']['usertype']['usertype'] == product['category']['usertype']['usertype']
        with allure.step("Проверить, что категория продукта соответствует ожидаемой"):
            assert product['category']['category'] == product['category']['category']
