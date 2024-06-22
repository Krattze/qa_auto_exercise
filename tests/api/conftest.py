import pytest
from endpoints.brand_list import BrandsListEndpoint
from endpoints.product_list import ProductListEndpoint
from endpoints.search_product import SearchProductEndpoint
from endpoints.user_detail import UserDetailsEndpoint
from endpoints.verify_login import VerifyLoginEndpoint




@pytest.fixture()
def brand_list_endpoint():
    return BrandsListEndpoint()


@pytest.fixture()
def product_list_endpoint():
    return ProductListEndpoint()


@pytest.fixture()
def search_product_endpoint():
    return SearchProductEndpoint()


@pytest.fixture()
def user_detail_endpoint():
    return UserDetailsEndpoint()


@pytest.fixture()
def verify_login_endpoint():
    return VerifyLoginEndpoint()





