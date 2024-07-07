import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from config import URL_RESET_PASSWORD


class ResetPasswordPage(BasePage):

    TEXT_ON_BUTTON_SAVE = 'Сохранить'

    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URL_RESET_PASSWORD

    def wait_for_load_page_reset_password(self):
        with allure.step('Ожидаем загрузки страницы "Восстановление пароля"'):
            self.wait_for_load_page()

    def get_text_on_page_reset_password(self):
        with allure.step('Получение текста со страницы "Восстановление пароля"'):
            self.scroll_to_element(ResetPasswordPageLocators.BUTTON_SAVE)
            return self.find_element(ResetPasswordPageLocators.BUTTON_SAVE).text

    def click_icon_field_password(self):
        with allure.step('Клик по кнопке показать/скрыть пароль в поле "Пароль" на странице "Восстановление пароля'):
            self.click_element(ResetPasswordPageLocators.ICON_FIELD_PASSWORD)

    def active_field_password(self):
        return self.wait_for_element_visible(ResetPasswordPageLocators.ACTIVE_FIELD_PASSWORD)
