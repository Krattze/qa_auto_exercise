from endpoints.base_endpoint import Endpoint
from utils.urls import Urls
import requests


class AccountEndpoint(Endpoint):

    def create_account(self, user):
        self.response = requests.post(Urls.CREATE_ACCOUNT_URL, data=user)
        self.response_json = self.response.json()

    def delete_account(self, creds):
        self.response = requests.delete(Urls.DELETE_ACCOUNT_URL, data=creds)
        self.response_json = self.response.json()