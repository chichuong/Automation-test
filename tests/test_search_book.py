# tests/test_book_search.py
import pytest
from pages.book_store_page import BookStorePage

@pytest.fixture(scope='class')
def search_keywords_from_data(test_data):
     keywords = test_data.get("search_keywords", [])
     assert keywords, "Không tìm thấy từ khóa tìm kiếm nào trong test_data.json"
     return keywords

@pytest.mark.usefixtures("driver")
class TestSearchBook:

    @pytest.fixture(autouse=True)
    def page_objects(self, driver):
        self.store_page = BookStorePage(driver)

    def test_search_books_and_verify(self, search_keywords_from_data, base_url):

        for keyword in search_keywords_from_data:
            print(f"\n--- Đang kiểm thử với từ khóa: '{keyword}' ---")
            self.store_page.navigate_to_book_store_from_home(base_url)
            self.store_page.search_book(keyword)
            try:
                verification_passed = self.store_page.verify_books_contain_keyword(keyword)
                assert verification_passed 
            except Exception as e:
                 pytest.fail(f"Kiểm thử thất bại cho từ khóa '{keyword}'. Lỗi: {e}", pytrace=False)

