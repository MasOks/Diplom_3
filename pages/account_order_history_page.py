import allure

from pages.base_page import BasePage
from locators.account_order_history_page_locators import AccountOrderHistoryPageLocators
from config import URL_ORDER_HISTORY


class AccountOrderHistoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_ORDER_HISTORY

    def wait_for_load_page_order_history(self):
        with allure.step('Ожидаем загрузки страницы "История заказов"'):
            self.wait_for_load_page()

    def get_order_ids(self):
        with allure.step('Получаем номера заказов пользователя из раздела "История заказов"'):
            order_numbers = list(
                order_number.text for order_number in self.wait_visible_elements(
                    AccountOrderHistoryPageLocators.ORDER_NUMBERS))
            return order_numbers
