from selenium.webdriver.common.by import By


class HomePageLocators:

    TEXT_IN_CONSTRUCTOR = [By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]/h1[text()='Соберите бургер']"]
    BURGER_INGREDIENTS = [By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]"]
    INGREDIENT_COUNTERS = [By.XPATH, ".//*[contains(@class, 'counter_counter__num')]"]

    SECTION_BASKET = [By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"]
    BUTTON_PLACE_AN_ORDER = [By.XPATH, ".//button[contains(@class, 'button_button') and text()='Оформить заказ']"]

    POP_UP_WINDOW_DETAILS_IS_OPENED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"]
    BUTTON_CLOSE_POP_UP_WINDOW = [
        By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"
    ]
    TEXT_NAME_INGREDIENT_IN_POP_UP_WINDOW_DETAILS = [
        By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div/div/p"
    ]

    ORDER_ID_IN_MODAL = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"]
    TEXT_ORDER_START_TO_PREPARE_IN_MODAL = [By.XPATH, ".//p[contains(@class, 'undefined text text_type_main-small')]"]
