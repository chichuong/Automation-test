import pytest
import os
from drivers.webdriver_factory import DriverFactory
from utils.data_loader import load_test_data

_test_data = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Trình duyệt để chạy kiểm thử: chrome, firefox, edge"
    )

@pytest.fixture(scope="session")
def test_data():
    global _test_data
    if _test_data is None:
        _test_data = load_test_data()
    return _test_data

@pytest.fixture(scope="session")
def driver(request, test_data): 
    browser_name = request.config.getoption("--browser")
    driver_instance = None
    try:
        driver_instance = DriverFactory.get_driver(browser_name)
        driver_instance.implicitly_wait(5)
        driver_instance.maximize_window()
        yield driver_instance
    except Exception as e:
        pytest.fail(f"Driver setup failed for {browser_name}: {e}")

    if driver_instance:
        driver_instance.quit()

@pytest.fixture(scope="session")
def base_url(test_data):
    return test_data.get("book_store_url", "https://demoqa.com/")