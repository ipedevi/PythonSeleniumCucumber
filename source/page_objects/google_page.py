from selenium.webdriver.common.by import By
from framework.basepage import BasePage

""" Path to the objects """
cookie_button_id = "L2AGLb"
search_box_name = "q"

""" Page Object functionality """
class google_page_object(BasePage):

    def accept_cookies(self):
        # Look for accept cookies button
        cookie_button = self.selenium_driver.find_element(By.ID, cookie_button_id)

        # Click on accept cookies button
        cookie_button.click()

    def find_text_in_google(self, text):
        # Look for find box
        search_box = self.selenium_driver.find_element(By.NAME, search_box_name)

        # Send the text to find
        search_box.send_keys(text)
        search_box.submit()