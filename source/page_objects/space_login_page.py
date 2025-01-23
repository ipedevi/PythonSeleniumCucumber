from selenium.webdriver.common.by import By
from framework.base_page import BasePage

""" Path to the objects """
user_input_xpath = "id('login')//input[contains(@type, 'text')]"
password_input_xpath = "id('login')//input[contains(@type, 'password')]"
login_page_button_xpath = "//button[contains(@form, 'login')]"

""" Page Object functionality """
class SpaceLoginPageObject(BasePage):

    def click_login_button(self):
        # Click on login button
        search_box = self.wait_for_element(lambda: self.selenium_driver.find_element(By.XPATH, login_page_button_xpath), 5)
        search_box.click()

    def add_username(self, user):
        # look for username field and send text
        user_field = self.wait_for_element(lambda: self.selenium_driver.find_element(By.XPATH, user_input_xpath), 5)
        user_field.send_keys(user)

    def add_password(self, pws):
        # look for password field and send text
        user_field = self.wait_for_element(lambda: self.selenium_driver.find_element(By.XPATH, password_input_xpath), 5)
        user_field.send_keys(pws)