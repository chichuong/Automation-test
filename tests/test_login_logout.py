import pytest
from drivers.webdriver_factory import DriverFactory
from pages.login_page import LoginPage

class TestLoginLogout:
    driver = None
    login_page = None

    @pytest.fixture(scope="class", autouse=True)
    def driver_setup(self):
        browser_to_test = "chrome"
        TestLoginLogout.driver = DriverFactory.get_driver(browser_to_test)  # ✅ sửa lại đúng class method
        TestLoginLogout.driver.maximize_window()
        TestLoginLogout.login_page = LoginPage(TestLoginLogout.driver)
        yield
        if TestLoginLogout.driver:
            TestLoginLogout.driver.quit()
            TestLoginLogout.driver = None

    USERNAME = "chichuong"
    PASSWORD = "Chuong@123"

    def test_successful_login_logout(self, driver_setup):
        self.login_page.go_to_login_page()
        self.login_page.login(self.USERNAME, self.PASSWORD)
        self.login_page.logout()
