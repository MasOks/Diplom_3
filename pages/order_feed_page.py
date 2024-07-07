import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from config import URL_ORDER_FEED


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_ORDER_FEED

    def open_page_order_feed(self):
        with allure.step(f'Переходим на страницу {self.URL}'):
            self.open_page(self.URL)

    def click_order_in_feed(self, index):
        with allure.step('Нажимаем на заказ в "Ленте заказов"'):
            orders = self.wait_visible_elements(OrderFeedPageLocators.LIST_ORDER_HISTORY)
            orders[index].click()

    def get_order_id_in_feed(self, index):
        with allure.step('Получаем номер заказа из "Ленты заказов"'):
            order_ids = self.wait_visible_elements(OrderFeedPageLocators.ORDER_IDS)
            return order_ids[index].text

    def get_list_order_ids(self):
        with allure.step('Получаем список с номерами заказов из "Ленты заказов"'):
            list_order_ids = list(
                order_id.text for order_id in self.wait_visible_elements(OrderFeedPageLocators.ORDER_IDS)
            )
            return list_order_ids

    def get_order_id_from_pop_up_window(self):
        with allure.step('Получаем номер заказа из всплывающего окна'):
            return self.wait_for_element_visible(OrderFeedPageLocators.ORDER_ID_IN_MODAL).text

    def get_quantity_completed_orders_for_all_time(self):
        with allure.step('Получаем значение счетчика "Выполнено за всё время"'):
            self.scroll_to_element(OrderFeedPageLocators.COUNTER_COMPLETED_ALL_TIME)
            return int(self.wait_for_element_visible(OrderFeedPageLocators.COUNTER_COMPLETED_ALL_TIME).text)

    def get_quantity_completed_orders_for_today(self):
        with allure.step('Получаем значение счетчика "Выполнено за сегодня"'):
            return int(self.wait_for_element_visible(OrderFeedPageLocators.COUNTER_COMPLETED_TODAY).text)

    def get_list_order_ids_in_progress(self):
        with allure.step('Получаем список с номерами заказов в разделе "В работе"'):
            return list(
                order_id.text for order_id in self.wait_visible_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
            )
