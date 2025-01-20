from selenium.common.exceptions import NoSuchElementException
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages,
     it also can include some specific tools like wait for element present"""

    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver

    def wait_for_element(self, element_finder, timeout: int = 10):
        """
        Waits for an element to exist in the DOM, checking every second.

        Args:
            element_finder (callable): A function or lambda that tries to locate the element.
            timeout (int): The maximum wait time in seconds.

        Returns:
            WebElement: The found element or False if it does not found.
        """
        end_time = time.time() + timeout

        while time.time() < end_time:
            try:
                # Try to find the element by calling the `element_finder` function
                element = element_finder()
                if element.is_displayed() and element.is_enabled():
                    return element

            except NoSuchElementException:
                # If the element is not found, wait for 1 second before retrying
                time.sleep(1)

        return False

