import allure
from framework.base_page import BasePage
from locators.space_locators import SpaceLocators


class SpacePageObject(BasePage):
    """Page object for the Space home page."""

    @allure.step("Click the login button")
    def click_login_button(self):
        """Waits for the login button to be clickable and clicks it."""
        search_box = self.wait_for_element(SpaceLocators.LOGIN_BUTTON)
        search_box.click()

    @allure.step("Check if the login button is displayed")
    def is_login_button_displayed(self):
        """Returns True if the login button is visible, False otherwise."""
        login_button = self.wait_for_element(SpaceLocators.LOGIN_BUTTON, 2)
        return login_button.is_displayed() if login_button else False
