import pytest
from endpoints.account import AccountEndpoint
from test_data.user import user


@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    # Блокировка запросов к рекламе
    context.route("**/*", lambda route, request: route.abort() if "pagead2.googlesyndication.com" in request.url else route.continue_())
    yield context
    context.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture()
def account_endpoint():
    return AccountEndpoint()


@pytest.fixture()
def create_test_user(account_endpoint):
    account_endpoint.create_account(user)


@pytest.fixture()
def delete_user_before_test(account_endpoint):
    account_endpoint.delete_account(user["email"], user["password"])


@pytest.fixture()
def delete_user_after_test(account_endpoint):
    yield
    account_endpoint.delete_account(user["email"], user["password"])


@pytest.fixture()
def create_and_delete_user_after_test(account_endpoint):
    account_endpoint.create_account(user)
    yield
    account_endpoint.delete_account(user["email"], user["password"])
