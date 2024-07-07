from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop


class BasePage:

    MODAL_WAIT_WINDOW = By.XPATH, "//*[@alt='loading animation']/parent::div"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def open_page(self, url: str):
        self.driver.get(url)

    def wait_for_load_page(self, timeout: int = 25):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(self.MODAL_WAIT_WINDOW))

    def find_element(self, locator, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within {timeout} seconds.')
            return None

    def click_element(self, locator, timeout: int = 30):
        self.wait_for_load_page()
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failed to enter text in element with locator {locator}.')

    def wait_visible_elements(self, locator, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f'Elements with locator {locator} not visible after {timeout} seconds.')
            return None

    def drag_and_drop(self, drag, drop):
        drag_and_drop(self.driver, drag, drop)

    def wait_for_element_visible(self, locator, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds.')
            return None

    def scroll_to_element(self, locator, timeout: int = 10):
        element = self.find_element(locator, timeout)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except TimeoutException:
            return None
