from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    _BOOK_STORE_CARD = (By.XPATH, "//h5[text()='Book Store Application']/ancestor::div[contains(@class,'top-card')]")
    _LOGIN_MENU_ITEM = (By.XPATH, "//div[contains(@class,'element-list') and contains(@class,'show')]//li[.//span[text()='Login']]")
    _USERNAME_INPUT = (By.ID, "userName")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login")
    _LOGOUT_BUTTON = (By.XPATH, "//button[@id='submit' and text()='Log out']")
    _LOGIN_HEADER = (By.XPATH, "//div[@class='main-header' and text()='Login']")
    _WELCOME_MESSAGE = (By.ID, "userName-value")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self, home_url):
        self.driver.get(home_url)
        self._find_element(self._BOOK_STORE_CARD)
        self.scroll_and_click(self._BOOK_STORE_CARD)
        self._find_element(self._LOGIN_MENU_ITEM) #
        self.scroll_and_click(self._LOGIN_MENU_ITEM)
        self._find_element(self._USERNAME_INPUT, EC.visibility_of_element_located) 

    def enter_username(self, username):
        self.enter_text(self._USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        self._find_element(self._LOGIN_BUTTON) 
        self.scroll_and_click(self._LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self.is_logout_button_visible() 

    def click_logout_button(self):
        self._find_element(self._LOGOUT_BUTTON)
        self.scroll_and_click(self._LOGOUT_BUTTON)

    def logout(self):
        self.click_logout_button()
        return self.is_element_visible(self._USERNAME_INPUT) 

    def is_logout_button_visible(self, timeout=10):
        return self.is_element_visible(self._LOGOUT_BUTTON, timeout)

    def get_welcome_message_user(self):
        return self.get_text(self._WELCOME_MESSAGE)