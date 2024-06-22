from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests


class ProductListEndpoint(Endpoint):

    def get_all_products(self):
        self.response = requests.get(Urls.PRODUCT_LIST_URL)
        self.response_json = self.response.json()

    def post_all_products(self):
        self.response = requests.post(Urls.PRODUCT_LIST_URL)
        self.response_json = self.response.json()

    def check_json_contains_product_list(self):
        assert "products" in self.response_json

    def check_product_list_contains_(self, product):
        products = self.response_json["products"]
        product = next((p for p in products if p['id'] == product['id']), None)
        assert product is not None
        assert product['name'] == product['name']
        assert product['price'] == product['price']
        assert product['brand'] == product['brand']
        assert product['category']['usertype']['usertype'] == product['category']['usertype']['usertype']
        assert product['category']['category'] == product['category']['category']
