# framework/base_test.py
import pytest
from framework.selenium_setup import SeleniumDriver
from features import myconfig

# Store driver globally for behave access
_global_driver = None


@pytest.fixture(scope="function")  # Fixture for each scenario
def selenium_driver():
    print("Initializing Selenium WebDriver from fixture...")
    config = myconfig.SELENIUM_CONFIG
    browser = config.get("browser", "chrome").lower()
    headless = config.get("headless", False)
    initial_page = config.get("initial_page", "https://www.google.com")

    selenium_setup = SeleniumDriver()
    driver = selenium_setup.start_driver(browser, headless, initial_page)

    global _global_driver
    print("Storing WebDriver globally...")
    _global_driver = driver  # Correctly store the driver instance

    yield driver


def prepare_driver():
    """
    Retrieve the initialized WebDriver.
    """
    print("Run pytest to initialize the fixture.")

    global _global_driver

    # Run pytest to initialize the fixture
    pytest.main(["-q", "--disable-warnings"])

    if not _global_driver:
        raise RuntimeError("Failed to initialize the Selenium WebDriver.")

    print("WebDriver retrieved successfully.")
    return _global_driver
