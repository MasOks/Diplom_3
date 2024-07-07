import allure

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from config import URL


class HomePage(BasePage):

    TEXT_ORDER_STARTED_PREPARE = 'Ваш заказ начали готовить'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL

    def wait_for_load_page_home(self):
        with allure.step('Ожидаем загрузки страницы'):
            self.wait_for_load_page()

    def click_ingredient_in_section_burger(self, index):
        with allure.step('Клик на ингредиент в разделе "Соберите бургер"'):
            ingredient = self.wait_visible_elements(HomePageLocators.BURGER_INGREDIENTS)
            ingredient[index].click()

    def get_ingredient_name_in_section_burger(self, index):
        with allure.step('Получаем наименование ингредиента в разделе "Соберите бургер"'):
            ingredients = self.wait_visible_elements(HomePageLocators.BURGER_INGREDIENTS)
            return ingredients[index].text.split('\n')[2]

    def wait_appearance_pop_up_window_with_ingredient_details(self):
        with allure.step('Появление на экране всплывающего окна "Детали ингредиента"'):
            return self.wait_for_element_visible(HomePageLocators.POP_UP_WINDOW_DETAILS_IS_OPENED)

    def get_ingredient_name_in_pop_up_window_with_details(self):
        with allure.step('Получаем наименование ингредиента во всплывающем окне "Детали ингредиента"'):
            return self.wait_for_element_visible(HomePageLocators.TEXT_NAME_INGREDIENT_IN_POP_UP_WINDOW_DETAILS).text

    def click_button_close_pop_up_window(self):
        with allure.step('Клик на крестик во всплывающем окне'):
            self.click_element(HomePageLocators.BUTTON_CLOSE_POP_UP_WINDOW)

    def add_ingredient_to_order(self, index):
        with allure.step('Добавляем ингредиент в корзину для оформления заказа'):
            ingredient = self.wait_visible_elements(HomePageLocators.BURGER_INGREDIENTS)
            basket = self.wait_for_element_visible(HomePageLocators.SECTION_BASKET)
            self.drag_and_drop(ingredient[index], basket)

    def get_value_counter_ingredient(self, index):
        with allure.step('Получаем значение счетчика ингредиента'):
            counter = self.wait_visible_elements(HomePageLocators.INGREDIENT_COUNTERS)
            return int(counter[index].text)

    def click_button_place_an_order(self):
        with allure.step('Клик на кнопку "Оформить заказ"'):
            self.click_element(HomePageLocators.BUTTON_PLACE_AN_ORDER)

    def get_order_id_in_pop_up_window(self):
        with allure.step('Получаем номер сформированного заказа из всплывающего окна о подтверждении заказа'):
            return f'0{self.find_element(HomePageLocators.ORDER_ID_IN_MODAL).text}'

    def get_text_order_in_pop_up_window(self):
        with allure.step('Получаем текст о формировании заказа из всплывающего окна о подтверждении заказа'):
            return self.wait_for_element_visible(HomePageLocators.TEXT_ORDER_START_TO_PREPARE_IN_MODAL).text
