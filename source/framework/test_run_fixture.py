from framework.base_test import selenium_driver

def test_initialize_selenium_driver(selenium_driver):
    """
    Dummy test to ensure the selenium_driver fixture runs.
    """
    print("Forcing to Run test to initialize Selenium WebDriver...")
    assert selenium_driver is not None, "Selenium driver did not initialize"
