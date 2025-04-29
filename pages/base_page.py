# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver, wait_timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_timeout)

    def _find_element(self, locator, condition=EC.presence_of_element_located):
        try:
            return self.wait.until(condition(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not found within timeout.")

    def _find_elements(self, locator, condition=EC.presence_of_all_elements_located):
        try:
            return self.wait.until(condition(locator))
        except TimeoutException:
            return []

    def click(self, locator):
        element = self._find_element(locator, EC.element_to_be_clickable)
        element.click()

    def enter_text(self, locator, text):
        element = self._find_element(locator, EC.visibility_of_element_located)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self._find_element(locator, EC.visibility_of_element_located)
        return element.text

    def get_elements_text(self, locator):
        elements = self._find_elements(locator, EC.visibility_of_all_elements_located)
        return [el.text for el in elements]

    def scroll_to_element(self, locator):
        try:
            element = self._find_element(locator, EC.presence_of_element_located)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except NoSuchElementException:
             raise

    def scroll_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click(locator)

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, substring, timeout=10):
        try:
            self.wait.until(EC.url_contains(substring))
            return True
        except TimeoutException:
            return False