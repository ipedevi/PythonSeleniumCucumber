class BasePage(object):
    """Base class to initialize the base page that will be called from all pages,
     it also can include some specific tools like wait for element present"""

    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver
