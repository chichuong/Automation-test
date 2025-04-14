from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    _HOME_URL = "https://demoqa.com/"
    _BOOK_STORE_CARD = (By.XPATH, "//h5[text()='Book Store Application']/ancestor::div[contains(@class,'top-card')]")
    _LOGIN_MENU_ITEM = (By.XPATH, "//div[contains(@class,'element-list') and contains(@class,'show')]//li[.//span[text()='Login']]")
    _USERNAME_INPUT = (By.ID, "userName")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login")
    _LOGOUT_BUTTON = (By.ID, "submit")
    _LOGIN_HEADER = (By.XPATH, "//div[@class='main-header' and text()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def scroll_and_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        clickable = self.wait.until(EC.element_to_be_clickable(locator))
        clickable.click()

    def go_to_login_page(self):
        self.driver.get(self._HOME_URL)
        self.scroll_and_click(self._BOOK_STORE_CARD)
        self.scroll_and_click(self._LOGIN_MENU_ITEM)
        self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))

    def enter_username(self, username):
        user_field = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        user_field.clear()
        user_field.send_keys(username)

    def enter_password(self, password):
        pass_field = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        pass_field.clear()
        pass_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        login_btn.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_logout_button()

    def click_logout_button(self):
        logout_btn = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_BUTTON))
        logout_btn.click()

    def logout(self):
        self.click_logout_button()
        self.wait_for_username_field()

    def wait_for_logout_button(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self._LOGOUT_BUTTON)
        )
        return True

    def wait_for_username_field(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self._USERNAME_INPUT)
        )
        return True
