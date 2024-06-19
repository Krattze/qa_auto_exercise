from endpoints.base_endpoint import Endpoint
from utils.urls import Urls
import requests


class VerifyLoginEndpoint(Endpoint):

    def verify_login(self, creds):
        self.response = requests.post(Urls.VERIFY_LOGIN_URL, data=creds)
        self.response_json = self.response.json()