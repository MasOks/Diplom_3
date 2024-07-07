from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    FIELD_EMAIL = [By.XPATH, ".//input[@type='text']"]
    BUTTON_RECOVER = [By.XPATH, ".//button[text()='Восстановить']"]
    HEADING_PAGE_FORGOT_PASSWORD = [By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2"]
