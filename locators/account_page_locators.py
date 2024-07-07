from selenium.webdriver.common.by import By


class AccountPageLocators:

    ORDERS_HISTORY = [By.XPATH, ".//a[@href='/account/order-history']"]
    BUTTON_EXIT = [By.XPATH, ".//button[contains(@class, 'Account_button')]"]
    TEXT_ON_ACCOUNT_PAGE = [By.XPATH, ".//p[contains(@class, 'Account_text')]"]
