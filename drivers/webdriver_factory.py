from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        browser_lower = browser_name.strip().lower()
        options = None

        if browser_lower == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser_lower == "firefox":
            options = webdriver.FirefoxOptions()
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        elif browser_lower == "edge":
            options = webdriver.EdgeOptions()
            service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        else:
            raise ValueError(f"Trình duyệt không được hỗ trợ: '{browser_name}'. Hỗ trợ: 'chrome', 'firefox', 'edge'.")
        return driver