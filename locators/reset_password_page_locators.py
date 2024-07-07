from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    ICON_FIELD_PASSWORD = [By.XPATH, ".//div[contains(@class, 'input__icon-action')]"]
    ACTIVE_FIELD_PASSWORD = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]
    BUTTON_SAVE = [By.XPATH, ".//form[contains(@class, 'Auth_form')]/button"]
