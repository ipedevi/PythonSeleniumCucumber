import allure
from selenium.webdriver.common.by import By
from framework.base_page import BasePage
from locators.space_checkout_locators import SpaceCheckoutLocators


class SpaceCheckoutPageObject(BasePage):
    """Page object for the checkout and promo code flow."""

    @allure.step("Navigate to '{url}'")
    def navigate_to(self, url):
        self.selenium_driver.get(url)

    @allure.step("Fill Name field with '{value}'")
    def fill_name(self, value):
        field = self.wait_for_element(SpaceCheckoutLocators.NAME_INPUT)
        field.clear()
        field.send_keys(value)

    @allure.step("Fill Email Address field with '{value}'")
    def fill_email(self, value):
        field = self.wait_for_element(SpaceCheckoutLocators.EMAIL_INPUT)
        field.clear()
        field.send_keys(value)

    @allure.step("Fill Social Security Number field with '{value}'")
    def fill_ssn(self, value):
        field = self.wait_for_element(SpaceCheckoutLocators.SSN_INPUT)
        field.clear()
        field.send_keys(value)

    @allure.step("Fill Phone Number field with '{value}'")
    def fill_phone(self, value):
        field = self.wait_for_element(SpaceCheckoutLocators.PHONE_INPUT)
        field.clear()
        field.send_keys(value)

    @allure.step("Check the terms and conditions checkbox")
    def check_terms(self):
        checkbox = self.wait_for_element(SpaceCheckoutLocators.TERMS_CHECKBOX)
        if not checkbox.is_selected():
             checkbox.click()

    @allure.step("Fill all required checkout fields")
    def fill_all_required_fields(self):
        self.fill_name("John Doe")
        self.fill_email("john@test.com")
        self.fill_ssn("123-45-6789")
        self.fill_phone("555-1234")

    @allure.step("Check if booking is completed successfully")
    def is_booking_completed(self):
        confirmation = self.wait_for_element(SpaceCheckoutLocators.BOOKING_CONFIRMATION, timeout=15)
        return confirmation is not False and confirmation.is_displayed()

    @allure.step("Check if button '{button_text}' is disabled")
    def is_button_disabled(self, button_text):
        xpath = SpaceCheckoutLocators.BUTTON_BY_TEXT.format(text=button_text)
        button = self.wait_for_element((By.XPATH, xpath))
        if button is False:
            return True
        disabled = button.get_attribute("disabled")
        return disabled is not None

    @allure.step("Get current order total price")
    def get_order_total(self):
        element = self.wait_for_element(SpaceCheckoutLocators.ORDER_TOTAL)
        return element.text.strip() if element else ""

    @allure.step("Enter promo code '{code}'")
    def fill_promo_code(self, code):
        field = self.wait_for_element(SpaceCheckoutLocators.PROMO_CODE_INPUT)
        field.clear()
        field.send_keys(code)

    @allure.step("Click the APPLY promo code button")
    def click_apply_button(self):
        button = self.wait_for_element(SpaceCheckoutLocators.APPLY_BUTTON)
        button.click()

    @allure.step("Check if BOOKED button is displayed for planet '{planet}'")
    def is_booked_button_displayed(self, planet):
        xpath = SpaceCheckoutLocators.BOOKED_BUTTON_BY_PLANET.format(planet=planet)
        result = self.wait_for_element((By.XPATH, xpath), timeout=5)
        return result is not False
