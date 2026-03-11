import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage(object):
    """Base class for all web page objects. Provides shared browser interaction utilities."""

    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver

    @allure.step("Wait for element {locator}")
    def wait_for_element(self, locator, timeout: int = 10):
        """
        Waits for an element to be visible and enabled in the DOM.

        Args:
            locator (tuple): A (By, value) tuple, e.g. (By.XPATH, "//button").
            timeout (int): The maximum wait time in seconds.

        Returns:
            WebElement: The found element, or False if not found within timeout.
        """
        try:
            return WebDriverWait(
                self.selenium_driver,
                timeout,
                ignored_exceptions=[StaleElementReferenceException]
            ).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
