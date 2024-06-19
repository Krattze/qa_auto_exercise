from endpoints.base_endpoint import Endpoint
from utils.urls import Urls
import requests


class SearchProductEndpoint(Endpoint):

    def search_product(self, product=None):
        data = {'search_product': product} if product else {}
        self.response = requests.post(Urls.SEARCH_PRODUCT_URL, data=data)
        self.response_json = self.response.json()