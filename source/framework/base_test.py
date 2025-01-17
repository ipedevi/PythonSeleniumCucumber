# framework/base_test.py
import pytest
from framework.selenium_setup import SeleniumDriver
from test import myconfig


class BaseTest:

    @pytest.fixture(scope="class", autouse=True)  # Fixture directamente aquí
    def selenium_driver(self, request):
        """ Read config from myconfig.py """
        config = myconfig.SELENIUM_CONFIG
        browser = config.get("browser", "chrome").lower()
        headless = config.get("headless", False)
        initial_page = config.get("initial_page", "https://www.google.es")
        driver = None

        """ The Fixture initialize and close the Selenium driver """
        selenium_setup = SeleniumDriver()
        driver = selenium_setup.start_driver(browser, headless, initial_page)
        # Assign driver to class instance (request.cls)
        request.cls.driver = driver
        yield driver
        selenium_setup.quit_driver()

    def setup_class(self):
        """Executed before all test in the class."""

    def teardown_class(self):
        """Executed after all test in the class."""
        pass  # Teardown managed automatically by fixture