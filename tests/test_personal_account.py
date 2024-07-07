import allure

from pages.header import Header
from pages.account_page import AccountPage
from pages.account_order_history_page import AccountOrderHistoryPage
from pages.login_page import LoginPage
from config import *


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на "Личный кабинет" в шапке сайта')
    def test_click_on_personal_account_link(self, web_driver, user, logining):
        header = Header(web_driver)
        header.click_on_personal_account()
        account_page = AccountPage(web_driver)
        account_page.wait_for_load_page_account()

        assert account_page.get_text_on_page_account() == account_page.TEXT_ON_PAGE_ACCOUNT

    @allure.title('Проверка перехода в раздел "История заказов" по клику на ссылку "История заказов" в личном кабинете')
    def test_click_on_order_history_link(self, web_driver, user, logining):
        header = Header(web_driver)
        header.click_on_personal_account()
        account_page = AccountPage(web_driver)
        account_page.wait_for_load_page_account()
        account_page.click_order_history()
        account_order_history_page = AccountOrderHistoryPage(web_driver)
        account_order_history_page.wait_for_load_page_order_history()

        assert account_order_history_page.current_url == URL_ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта по клику на кнопку "Выход" в личном кабинете')
    def test_exit_from_personal_account(self, web_driver, user, logining):
        header = Header(web_driver)
        header.click_on_personal_account()
        account_page = AccountPage(web_driver)
        account_page.wait_for_load_page_account()
        account_page.click_button_exit()
        login_page = LoginPage(web_driver)
        login_page.wait_for_load_page_login()

        assert login_page.get_text_heading() == login_page.TEXT_HEADING
