import allure
from framework.base_api_page import BaseApiPage
from locators.dog_api_locators import DogApiLocators


class DogApiPageObject(BaseApiPage):
    """Page object for TheDogApi."""

    @allure.step("GET random dog image")
    def get_random_image(self):
        """Requests a random dog image and returns the response."""
        return self.send_api("GET", DogApiLocators.RANDOM_IMAGE)

    @allure.step("Extract image URL from response")
    def get_image_url(self, response):
        """Returns the image URL from the first result in the response."""
        return response.json()[0]['url']
