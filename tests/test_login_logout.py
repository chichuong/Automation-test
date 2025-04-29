# tests/test_login.py
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLoginLogout:

    @pytest.fixture(autouse=True)
    def page_objects(self, driver):
        self.login_page = LoginPage(driver)

    def test_successful_login_logout(self, test_data, base_url):
        credentials = test_data['login_credentials']['valid_user']
        username = credentials['username']
        password = credentials['password']


        self.login_page.go_to_login_page(base_url)

        # Đăng nhập
        login_success = self.login_page.login(username, password)
        assert login_success, "Đăng nhập thất bại: Không thấy nút Logout sau khi đăng nhập."

        # Xác minh username 
        displayed_user = self.login_page.get_welcome_message_user()
        assert displayed_user == username, \
            f"Tên người dùng đăng nhập không khớp. Mong đợi '{username}', nhận được '{displayed_user}'"

        # Đăng xuất
        logout_success = self.login_page.logout()
        assert logout_success, "Đăng xuất thất bại: Không thấy trường nhập username sau khi đăng xuất."
