from selenium.webdriver.common.by import By
from framework.base_page import BasePage

""" Path to the objects """
login_button_xpath = "//button[contains(@class, 'NavButton')]"

""" Page Object functionality """
class SpacePageObject(BasePage):

    def click_login_button(self):
        # Click on login button
        search_box = self.selenium_driver.find_element(By.XPATH, login_button_xpath)
        search_box.click()

    def is_login_button_displayed(self):
        # Check if login button exists
        login_button = self.wait_for_element(lambda:self.selenium_driver.find_element(By.XPATH, login_button_xpath), 2)
        return login_button.is_displayed() if login_button else False
