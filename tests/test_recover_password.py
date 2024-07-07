import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestRecoverPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_on_recover_password_link(self, web_driver):
        login_page = LoginPage(web_driver)
        login_page.open_page_login()
        login_page.wait_for_load_page_login()
        login_page.click_link_recover_password()
        forgot_page = ForgotPasswordPage(web_driver)
        forgot_page.wait_for_load_page_forgot_password()

        assert forgot_page.get_text_on_page_forgot_password() == forgot_page.TEXT_HEADING_FORGOT_PASSWORD

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить" на странице восстановления пароля')
    def test_enter_email_and_click_recover_button(self, web_driver, user):
        forgot_page = ForgotPasswordPage(web_driver)
        forgot_page.open_page_forgot_password()
        forgot_page.enter_text_in_field_email(user['email'])
        forgot_page.click_button_recover()
        reset_page = ResetPasswordPage(web_driver)
        reset_page.wait_for_load_page_reset_password()

        assert reset_page.get_text_on_page_reset_password() == reset_page.TEXT_ON_BUTTON_SAVE

    @allure.title("Проверка клика по кнопке показать/скрыть пароль (делает поле активным — подсвечивает его)")
    def test_click_on_show_hide_password_button_makes_field_active(self, web_driver, user):
        forgot_page = ForgotPasswordPage(web_driver)
        forgot_page.open_page_forgot_password()
        forgot_page.enter_text_in_field_email(user['email'])
        forgot_page.click_button_recover()
        reset_page = ResetPasswordPage(web_driver)
        reset_page.wait_for_load_page_reset_password()
        reset_page.click_icon_field_password()
        field_password = reset_page.active_field_password()

        assert 'input_status_active' in field_password.get_attribute('class')
