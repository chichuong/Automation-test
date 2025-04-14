import pytest
from drivers.webdriver_factory import DriverFactory

@pytest.fixture(params=["chrome"])  
def setup_driver(request):
    driver = DriverFactory.get_driver(request.param)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
