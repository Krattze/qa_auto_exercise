from endpoints.base_endpoint import Endpoint
from utils.urls import Urls
import requests


class BrandsListEndpoint(Endpoint):

    def get_all_brands(self):
        self.response = requests.get(Urls.BRAND_LIST_URL)
        self.response_json = self.response.json()

    def put_all_brands(self):
        self.response = requests.post(Urls.PRODUCT_LIST_URL)
        self.response_json = self.response.json()

    def check_json_contains_brands_list(self):
        assert "brands" in self.response_json
