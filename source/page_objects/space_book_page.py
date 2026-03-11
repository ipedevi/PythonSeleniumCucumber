import allure
from selenium.webdriver.common.by import By
from framework.base_page import BasePage
from locators.space_book_locators import SpaceBookLocators


class SpaceBookPageObject(BasePage):
    """Page object for the planet booking flow on the Space home page."""

    @allure.step("Click the BOOK button for planet '{planet}'")
    def click_book_for_planet(self, planet):
        """Finds the BOOK button next to the given planet name and clicks it."""
        xpath = SpaceBookLocators.BOOK_BUTTON_BY_PLANET.format(planet=planet)
        button = self.wait_for_element((By.XPATH, xpath))
        button.click()

    @allure.step("Check if destination '{planet}' is available")
    def is_destination_available(self, planet):
        """Returns True if a BOOK button exists for the given planet, False otherwise."""
        xpath = SpaceBookLocators.BOOK_BUTTON_BY_PLANET.format(planet=planet)
        result = self.wait_for_element((By.XPATH, xpath), 3)
        return result is not False

    @allure.step("Check if the trip price is displayed")
    def is_price_displayed(self):
        """Returns True if the trip price element is visible on the confirmation page."""
        price = self.wait_for_element(SpaceBookLocators.TRIP_PRICE)
        return price.is_displayed() if price else False
