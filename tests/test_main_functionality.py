import allure

from pages.header import Header
from pages.home_page import HomePage


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на ссылку "Конструктор" в шапке сайта')
    def test_click_on_constructor_link(self, web_driver):
        header = Header(web_driver)
        header.click_on_order_feed()
        header.click_on_constructor()
        header.wait_for_load_constructor()

        assert header.get_text_in_constructor() == header.TEXT_HEADING_IN_CONSTRUCTOR

    @allure.title('Проверка перехода по клику на ссылку "Лента заказов" в шапке сайта')
    def test_click_on_order_feed_link(self, web_driver):
        header = Header(web_driver)
        header.click_on_order_feed()
        header.wait_for_load_order_feed()

        assert header.get_text_in_order_feed() == header.TEXT_HEADING_IN_ORDER_FEED

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_appearance_pop_up_window_with_details_by_click_on_ingredient(self, web_driver):
        home_page = HomePage(web_driver)
        ingredient_name = home_page.get_ingredient_name_in_section_burger(1)
        home_page.click_ingredient_in_section_burger(1)
        home_page.wait_appearance_pop_up_window_with_ingredient_details()

        assert home_page.get_ingredient_name_in_pop_up_window_with_details() == ingredient_name

    @allure.title('Проверка закрытия всплывающего окна с деталями при клике на крестик')
    def test_close_pop_up_window_with_details_by_click_button_close(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.wait_for_load_page_home()
        home_page.click_ingredient_in_section_burger(0)
        pop_up_window = home_page.wait_appearance_pop_up_window_with_ingredient_details()
        home_page.click_button_close_pop_up_window()

        assert 'Modal_modal_opened' not in pop_up_window.get_attribute('class')

    @allure.title('Проверка, что при добавлении ингредиента в заказ, счетчик этого ингредиента увеличивается')
    def test_counter_increases_when_ingredient_added_in_order(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.wait_for_load_page_home()
        counter_before = home_page.get_value_counter_ingredient(1)
        home_page.add_ingredient_to_order(1)
        counter_after = home_page.get_value_counter_ingredient(1)

        assert counter_after > counter_before

    @allure.title('Проверка залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_an_order(self, web_driver, user, logining):
        home_page = HomePage(web_driver)
        home_page.add_ingredient_to_order(0)
        home_page.add_ingredient_to_order(3)
        home_page.add_ingredient_to_order(12)
        home_page.click_button_place_an_order()
        home_page.click_button_close_pop_up_window()

        assert home_page.get_text_order_in_pop_up_window() == home_page.TEXT_ORDER_STARTED_PREPARE
