from endpoints.base_endpoint import Endpoint
from test_data.urls import Urls
import requests


class VerifyLoginEndpoint(Endpoint):

    def verify_login(self, creds):
        creds = {
            'email': f"{creds['email']}",
            'password': f"{creds['password']}"
        }
        self.response = requests.post(Urls.VERIFY_LOGIN_URL, data=creds)
        self.response_json = self.response.json()
