# framework/selenium_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class SeleniumDriver:

    def start_driver(self, browser, headless, initial_page):
        # Depends on the browser, the selenium driver is opened
        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=FirefoxService(), options=options)

        # We only are managing chrome and firefox (if not is an error)
        else:
            raise ValueError(f"Navegador no soportado: {browser}")

        # After driver load, the initial page is loaded
        self.driver.get(initial_page)

        self.driver.maximize_window()
        return self.driver

    # def quit_driver(self):
    #     if self.driver:
    #         self.driver.quit()

