from endpoints.base_endpoint import Endpoint
from utils.urls import Urls
import requests


class UserDetailsEndpoint(Endpoint):

    def get_user_details(self, email=None):
        data = {'email': email} if email else {}
        self.response = requests.get(Urls.USER_DETAIL_URL, params=data)
        self.response_json = self.response.json()
        print(self.response_json)