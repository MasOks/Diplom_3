from selenium.webdriver.common.by import By


class AccountOrderHistoryPageLocators:

    ORDER_NUMBERS = [
        By.XPATH,
        ".//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, '_digits') and contains(text(), '#')]"
    ]
