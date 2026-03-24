from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class SeleniumDriver:

    def start_driver(self, browser, headless, initial_page, remote_url=None):
        if browser == "chrome_local":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")   # 👈 importante (nuevo headless)

            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")  # 👈 ESTE ES EL CLAVE
            self.driver = webdriver.Chrome(service=ChromeService(), options=options)

        elif browser == "firefox_local":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=FirefoxService(), options=options)

        elif browser == "chrome_remote":
            options = ChromeOptions()
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            self.driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

        elif browser == "firefox_remote":
            options = FirefoxOptions()
            self.driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

        else:
            raise ValueError(f"Browser not supported: {browser}. Use chrome_local, firefox_local, chrome_remote or firefox_remote.")

        self.driver.get(initial_page)
        self.driver.maximize_window()
        return self.driver
