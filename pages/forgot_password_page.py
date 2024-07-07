import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from config import URL_FORGOT_PASSWORD


class ForgotPasswordPage(BasePage):

    TEXT_HEADING_FORGOT_PASSWORD = 'Восстановление пароля'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_FORGOT_PASSWORD

    def open_page_forgot_password(self):
        with allure.step(f'Переходим на страницу {self.URL}'):
            self.open_page(self.URL)

    def wait_for_load_page_forgot_password(self):
        with allure.step('Ожидаем загрузки страницы "Восстановление пароля"'):
            self.wait_for_load_page()

    def get_text_on_page_forgot_password(self):
        with allure.step('Получение текста со страницы "Восстановление пароля"'):
            self.scroll_to_element(ForgotPasswordPageLocators.HEADING_PAGE_FORGOT_PASSWORD)
            return self.find_element(ForgotPasswordPageLocators.HEADING_PAGE_FORGOT_PASSWORD).text

    def enter_text_in_field_email(self, email):
        with allure.step('Вводим email пользователя в поле "Email" на странице восстановления пароля'):
            self.enter_text(ForgotPasswordPageLocators.FIELD_EMAIL, email)

    def click_button_recover(self):
        with allure.step('Нажимаем кнопку "Восстановить" на странице восстановления пароля'):
            self.click_element(ForgotPasswordPageLocators.BUTTON_RECOVER)
