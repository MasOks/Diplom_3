from selenium.webdriver.common.by import By


class LoginPageLocators:

    FIELD_EMAIL = [By.XPATH, ".//input[@type='text']"]
    FIELD_PASSWORD = [By.XPATH, ".//input[@type='password']"]
    BUTTON_ENTER = [By.XPATH, ".//button[text()='Войти']"]
    RECOVER_PASSWORD = [By.XPATH, ".//a[@href='/forgot-password']"]
    HEADING_PAGE = [By.XPATH, ".//h2[text()='Вход']"]
