import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import URL_LOGIN


class LoginPage(BasePage):

    TEXT_HEADING = 'Вход'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_LOGIN

    def open_page_login(self):
        with allure.step(f'Переходим на страницу {self.URL}'):
            self.open_page(self.URL)

    def wait_for_load_page_login(self):
        with allure.step('Ожидаем загрузки страницы "Вход"'):
            self.wait_for_load_page()

    def enter_text_in_field_email(self, email):
        with allure.step('Заполняем поле "Email" на странице "Вход"'):
            self.enter_text(LoginPageLocators.FIELD_EMAIL, email)

    def enter_text_in_field_password(self, password):
        with allure.step('Заполняем поле "Пароль" на странице "Вход"'):
            self.enter_text(LoginPageLocators.FIELD_PASSWORD, password)

    def click_button_enter(self):
        with allure.step('Нажимаем на кнопку "Войти" на странице "Вход"'):
            self.click_element(LoginPageLocators.BUTTON_ENTER)

    def click_link_recover_password(self):
        with allure.step('Нажимаем на ссылку "Восстановить пароль" на странице "Вход"'):
            self.click_element(LoginPageLocators.RECOVER_PASSWORD)

    def enter_in_system(self, payload):
        with allure.step('Вход в систему (ввод данных на странице "Вход")'):
            self.enter_text_in_field_email(payload['email'])
            self.enter_text_in_field_password(payload['password'])
            self.click_button_enter()

    def get_text_heading(self):
        with allure.step('Получение текста заголовка страницы'):
            self.scroll_to_element(LoginPageLocators.HEADING_PAGE)
            return self.find_element(LoginPageLocators.HEADING_PAGE).text
