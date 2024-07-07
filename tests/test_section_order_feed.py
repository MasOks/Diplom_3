import allure

from pages.order_feed_page import OrderFeedPage
from pages.home_page import HomePage
from pages.header import Header
from pages.account_page import AccountPage
from pages.account_order_history_page import AccountOrderHistoryPage


class TestSectionOrderFeed:

    @allure.title('Проверка открытия всплывающего окна с деталями по клику на заказ в разделе "Лента заказов"')
    def test_opening_pop_up_window_details_by_click_on_order(self, web_driver):
        order_feed = OrderFeedPage(web_driver)
        order_feed.open_page_order_feed()
        order_id = order_feed.get_order_id_in_feed(0)
        order_feed.click_order_in_feed(0)

        assert order_feed.get_order_id_from_pop_up_window() == order_id

    @allure.title('Проверка отображения заказов пользователя из раздела "История заказов" на странице "Лента заказов"')
    def test_display_user_orders_from_order_history_section_on_order_feed_page(self, web_driver, user, logining):
        home_page = HomePage(web_driver)
        home_page.add_ingredient_to_order(0)
        home_page.add_ingredient_to_order(3)
        home_page.add_ingredient_to_order(12)
        home_page.click_button_place_an_order()
        home_page.click_button_close_pop_up_window()
        header = Header(web_driver)
        header.click_on_personal_account()
        account_page = AccountPage(web_driver)
        account_page.wait_for_load_page_account()
        account_page.click_order_history()
        order_history_page = AccountOrderHistoryPage(web_driver)
        order_ids_from_order_history = order_history_page.get_order_ids()
        order_feed = OrderFeedPage(web_driver)
        order_feed.open_page_order_feed()
        order_ids_from_order_feed = order_feed.get_list_order_ids()
        for order_id in order_ids_from_order_history:

            assert order_id in order_ids_from_order_feed

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_increases_completed_for_all_time_counter_when_creating_new_order(self, web_driver, user, logining):
        header = Header(web_driver)
        header.click_on_order_feed()
        order_feed = OrderFeedPage(web_driver)
        counter_before = order_feed.get_quantity_completed_orders_for_all_time()
        header.click_on_constructor()
        home_page = HomePage(web_driver)
        home_page.add_ingredient_to_order(0)
        home_page.add_ingredient_to_order(3)
        home_page.add_ingredient_to_order(12)
        home_page.click_button_place_an_order()
        home_page.click_button_close_pop_up_window()
        header.click_on_order_feed()
        counter_after = order_feed.get_quantity_completed_orders_for_all_time()

        assert counter_after > counter_before

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_increases_completed_for_today_counter_when_creating_new_order(self, web_driver, user, logining):
        header = Header(web_driver)
        header.click_on_order_feed()
        order_feed = OrderFeedPage(web_driver)
        counter_before = order_feed.get_quantity_completed_orders_for_today()
        header.click_on_constructor()
        home_page = HomePage(web_driver)
        home_page.add_ingredient_to_order(0)
        home_page.add_ingredient_to_order(3)
        home_page.add_ingredient_to_order(12)
        home_page.click_button_place_an_order()
        home_page.click_button_close_pop_up_window()
        header.click_on_order_feed()
        counter_after = order_feed.get_quantity_completed_orders_for_today()

        assert counter_after > counter_before

    @allure.title('Проверка появления номера заказа в разделе "В работе" после его оформления')
    def test_appearance_order_id_in_section_in_progress_after_place_an_order(self, web_driver, user, logining):
        home_page = HomePage(web_driver)
        home_page.add_ingredient_to_order(0)
        home_page.add_ingredient_to_order(3)
        home_page.add_ingredient_to_order(12)
        home_page.click_button_place_an_order()
        home_page.click_button_close_pop_up_window()
        order_id = home_page.get_order_id_in_pop_up_window()
        header = Header(web_driver)
        header.click_on_order_feed()
        order_feed = OrderFeedPage(web_driver)
        order_ids_in_progress = order_feed.get_list_order_ids_in_progress()

        assert order_id in order_ids_in_progress
