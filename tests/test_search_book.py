import pytest
from pages.book_store_page import BookStorePage

class TestSearchBook:

    @pytest.mark.parametrize("keyword", ["java"])
    def test_search_books_with_keyword(self, setup_driver, keyword):
        driver = setup_driver
        store = BookStorePage(driver)

        driver.get("https://demoqa.com/")
        store.navigate_to_book_store()
        store.search_book(keyword)
        store.verify_books_contain(keyword) 

