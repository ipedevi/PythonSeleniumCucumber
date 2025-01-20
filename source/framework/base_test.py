# framework/base_test.py
from framework.selenium_setup import SeleniumDriver
from features import myconfig


class BaseTest:
    driver = None  # Driver shared between scenarios

    @staticmethod
    def start_selenium_driver():

        # Starting selenium webdriver
        config = myconfig.SELENIUM_CONFIG
        browser = config.get("browser", "chrome").lower()
        headless = config.get("headless", False)
        initial_page = config.get("initial_page", "https://www.google.es")
        selenium_setup = SeleniumDriver()
        driver = selenium_setup.start_driver(browser, headless, initial_page)
        return driver

    @staticmethod
    def quit_selenium_driver(driver):
        # Closing selenium webdriver
        if driver:
            driver.quit()
