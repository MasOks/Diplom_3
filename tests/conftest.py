import pytest
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from config import URL
from pages.login_page import LoginPage


def _get_driver(name):
    if name == 'chrome':
        from selenium.webdriver.chrome.service import Service as ChromeService

        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == 'firefox':
        return webdriver.Firefox()
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(params=['chrome', 'firefox'])
def web_driver(request):
    driver = _get_driver(request.param)
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def user():
    fake = Faker(locale='ru_RU')
    user_data = {
        "email": fake.email(),
        "password": fake.password(length=9, special_chars=False),
        "name": fake.name()
    }
    try:
        response = requests.post(f'{URL}/api/auth/register', json=user_data)
    except requests.RequestException as e:
        raise e
    else:
        access_token = response.json()['accessToken']
        del user_data['name']

        yield user_data

        headers = {"Authorization": access_token}
        requests.delete(f'{URL}/api/auth/user', headers=headers)


@pytest.fixture()
def login_page(web_driver):
    return LoginPage(web_driver)


@pytest.fixture()
def logining(login_page, user):
    login_page.open_page_login()
    login_page.enter_in_system(user)
