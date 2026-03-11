from framework.selenium_setup import SeleniumDriver
import myconfig


class WebSession:
    """
    Manages a browser session for a test scenario.
    Encapsulates the driver so additional context (e.g. multiple drivers,
    shared state) can be added here without touching the test layer.
    """

    def __init__(self):
        config = myconfig.SELENIUM_CONFIG
        self._browser = config.get("browser", "chrome_local").lower()
        self._headless = config.get("headless", False)
        self._initial_page = config.get("initial_page", "https://www.google.com")
        self._remote_url = config.get("remote_url", None)
        self.driver = None

    def start_driver(self):
        self.driver = SeleniumDriver().start_driver(
            self._browser, self._headless, self._initial_page, self._remote_url
        )
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
