from selenium.webdriver.common.by import By


class HeaderLocators:

    CONSTRUCTOR = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/']"]
    ORDER_FEED = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/feed']"]
    PERSONAL_ACCOUNT = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/account']"]
