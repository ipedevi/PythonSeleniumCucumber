import allure
from framework.base_page import BasePage
from locators.space_login_locators import SpaceLoginLocators


class SpaceLoginPageObject(BasePage):
    """Page object for the Space login form."""

    @allure.step("Click the submit button on the login form")
    def click_login_button(self):
        """Waits for the form submit button and clicks it."""
        search_box = self.wait_for_element(SpaceLoginLocators.LOGIN_BUTTON, 5)
        search_box.click()

    @allure.step("Enter username '{user}'")
    def add_username(self, user):
        """Waits for the username field and types the given value."""
        user_field = self.wait_for_element(SpaceLoginLocators.USER_INPUT, 5)
        user_field.send_keys(user)

    @allure.step("Enter password")
    def add_password(self, pws):
        """Waits for the password field and types the given value."""
        user_field = self.wait_for_element(SpaceLoginLocators.PASSWORD_INPUT, 5)
        user_field.send_keys(pws)

    @allure.step("Check if the missing username error is displayed")
    def is_username_error_displayed(self):
        """Returns True if the error for missing username is visible, False otherwise."""
        error = self.wait_for_element(SpaceLoginLocators.USERNAME_ERROR, 5)
        return error.is_displayed() if error else False

    @allure.step("Check if the missing password error is displayed")
    def is_password_error_displayed(self):
        """Returns True if the error for missing password is visible, False otherwise."""
        error = self.wait_for_element(SpaceLoginLocators.PASSWORD_ERROR, 5)
        return error.is_displayed() if error else False
