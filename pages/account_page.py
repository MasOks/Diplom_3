import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from config import URL_ACCOUNT


class AccountPage(BasePage):

    TEXT_ON_PAGE_ACCOUNT = 'В этом разделе вы можете изменить свои персональные данные'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_ACCOUNT

    def wait_for_load_page_account(self):
        with allure.step('Ожидаем загрузки страницы "Личного кабинета"'):
            self.wait_for_load_page()

    def get_text_on_page_account(self):
        with allure.step('Получение текста со страницы "Личного кабинета"'):
            self.scroll_to_element(AccountPageLocators.TEXT_ON_ACCOUNT_PAGE)
            return self.find_element(AccountPageLocators.TEXT_ON_ACCOUNT_PAGE).text

    def click_order_history(self):
        with allure.step('Переходим в историю заказов при клике на ссылку "История заказов" в "Личном кабинете"'):
            self.click_element(AccountPageLocators.ORDERS_HISTORY)

    def click_button_exit(self):
        with allure.step('Выходим из аккаунта при клике на кнопку "Выход" в "Личном кабинете"'):
            self.click_element(AccountPageLocators.BUTTON_EXIT)
