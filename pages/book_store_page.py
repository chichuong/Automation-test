# pages/book_store_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class BookStorePage(BasePage):
    _HOME_BOOK_STORE_CARD = (By.XPATH, "//h5[text()='Book Store Application']/ancestor::div[contains(@class,'top-card')]")
    _LEFT_PANEL_BOOK_STORE_MENU = (By.XPATH, "//div[contains(@class,'element-list') and contains(@class,'show')]//li[.//span[text()='Book Store']]")
    _SEARCH_BOX = (By.ID, "searchBox")
    _BOOK_TITLES_LINKS = (By.XPATH, "//div[@class='rt-tr-group']//div[@class='action-buttons']//a")
    _NO_ROWS_FOUND_MSG = (By.XPATH, "//div[@class='rt-noData']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_book_store_from_home(self, home_url):
        self.driver.get(home_url)
        self._find_element(self._HOME_BOOK_STORE_CARD)
        self.scroll_and_click(self._HOME_BOOK_STORE_CARD)
        self._find_element(self._LEFT_PANEL_BOOK_STORE_MENU) 
        self.scroll_and_click(self._LEFT_PANEL_BOOK_STORE_MENU)
        self._find_element(self._SEARCH_BOX, EC.visibility_of_element_located) 

    def search_book(self, keyword):
        self.enter_text(self._SEARCH_BOX, keyword)


    def get_visible_book_titles(self):
        if self.is_element_visible(self._NO_ROWS_FOUND_MSG, timeout=1):
            print("Không tìm thấy sách nào khớp với tìm kiếm.") 
            return []
        self._find_element(self._BOOK_TITLES_LINKS, EC.presence_of_element_located)
        return self.get_elements_text(self._BOOK_TITLES_LINKS)

    def verify_books_contain_keyword(self, keyword):
        titles = self.get_visible_book_titles()
        assert len(titles) > 0, f"Không tìm thấy sách nào cho từ khóa: {keyword}"

        missing = []
        keyword_lower = keyword.lower()
        for title in titles:
            print(f"Found book: {title}")
            if keyword_lower not in title.lower():
                missing.append(title)

        assert not missing, \
            f"Từ khóa '{keyword}' không được tìm thấy trong các tiêu đề sách sau: {', '.join(missing)}"
        return True