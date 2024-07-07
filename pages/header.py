import allure

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from config import URL


class Header(BasePage):

    TEXT_HEADING_IN_CONSTRUCTOR = 'Соберите бургер'
    TEXT_HEADING_IN_ORDER_FEED = 'Лента заказов'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL

    def wait_for_load_constructor(self):
        with allure.step('Ожидаем загрузки "Конструктора"'):
            self.wait_for_load_page()

    def click_on_constructor(self):
        with allure.step('Проверяем переход по клику на "Конструктор" в шапке сайта'):
            self.click_element(HeaderLocators.CONSTRUCTOR)

    def click_on_order_feed(self):
        with allure.step('Проверяем переход по клику на "Лента заказов" в шапке сайта'):
            self.click_element(HeaderLocators.ORDER_FEED)

    def wait_for_load_order_feed(self):
        with allure.step('Ожидаем загрузки "Ленты заказов"'):
            self.wait_for_load_page()

    def click_on_personal_account(self):
        with allure.step('Проверяем переход по клику на "Личный кабинет" в шапке сайта'):
            self.click_element(HeaderLocators.PERSONAL_ACCOUNT)

    def get_text_in_constructor(self):
        with allure.step('Получение текста заголовка в "Конструкторе"'):
            self.scroll_to_element(HomePageLocators.TEXT_IN_CONSTRUCTOR)
            return self.find_element(HomePageLocators.TEXT_IN_CONSTRUCTOR).text

    def get_text_in_order_feed(self):
        with allure.step('Получение текста заголовка в "Ленте заказов"'):
            self.scroll_to_element(OrderFeedPageLocators.TEXT_IN_ORDER_FEED)
            return self.find_element(OrderFeedPageLocators.TEXT_IN_ORDER_FEED).text
