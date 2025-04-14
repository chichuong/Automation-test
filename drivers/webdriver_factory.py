from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome"):
        browser_lower = browser_name.strip().lower()

        if browser_lower == "chrome":
            options = webdriver.ChromeOptions()
            service = ChromeService(executable_path=ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)

        elif browser_lower == "firefox":
            options = webdriver.FirefoxOptions()
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: '{browser_name}'. Use 'chrome' or 'firefox'.")
