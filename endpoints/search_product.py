from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests
import allure


class SearchProductEndpoint(Endpoint):

    @allure.step("Выполнить поиск продукта")
    def search_product(self, product=None):
        data = {'search_product': product} if product else {}
        with allure.step("POST запрос на search_product endpoint с данными: {data}"):
            self.response = requests.post(Urls.SEARCH_PRODUCT_URL, data=data)
            self.response_json = self.response.json()

    @allure.step("Проверить, что категория продукта совпадает с категорий поиска")
    def check_product_category_equal_search_name(self, product_to_search, have_products):
        if have_products:
            for product in self.response_json["products"]:
                assert product_to_search.lower() in product["category"]["category"].lower()
        else:
            assert len(self.response_json["products"]) == 0
