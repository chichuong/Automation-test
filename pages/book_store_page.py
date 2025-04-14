from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookStorePage:
    _BOOK_STORE_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][1]")
    _ELEMENTS_GROUP = (By.XPATH, "//div[@class='element-group'][6]")
    _BOOK_STORE_MENU = (By.XPATH, "//li[.//span[text()='Book Store']]")
    _SEARCH_BOX = (By.ID, "searchBox")
    _BOOK_TITLES = (By.XPATH, "//div[@class='rt-tr-group']//div[@class='action-buttons']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def navigate_to_book_store(self):
        self.click(self._BOOK_STORE_CARD)
        self.scroll_to_element(self._ELEMENTS_GROUP)
        self.click(self._ELEMENTS_GROUP)
        self.click(self._BOOK_STORE_MENU)

    def search_book(self, keyword):
        self.enter_text(self._SEARCH_BOX, keyword)

    def get_book_titles(self):
        return [el.text for el in self.get_elements(self._BOOK_TITLES)]

    def verify_books_contain(self, keyword):
        books = self.get_book_titles()
        for book in books:
            assert keyword.lower() in book.lower()
