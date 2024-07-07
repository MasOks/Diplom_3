from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    TEXT_IN_ORDER_FEED = [
        By.XPATH, ".//main[contains(@class, 'App_componentContainer')]/div/h1[text()='Лента заказов']"
    ]

    LIST_ORDER_HISTORY = [By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]"]

    ORDER_IDS = [
        By.XPATH,
        ".//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, '_digits') and contains(text(), '#')]"
    ]

    ORDERS_IN_PROGRESS = [
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text text_type_digits-default')]"
    ]

    COUNTER_COMPLETED_ALL_TIME = [
        By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'OrderFeed_number')]"
    ]

    COUNTER_COMPLETED_TODAY = [
        By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[contains(@class, 'OrderFeed_number')]"
    ]

    ORDER_ID_IN_MODAL = [
        By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]/p[contains(@class, 'text text_type_digits-default')]"
    ]
