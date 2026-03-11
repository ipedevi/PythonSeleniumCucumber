import allure
import requests


class BaseApiPage(object):
    """Base class for all API page objects. Provides shared HTTP request utilities."""

    def __init__(self, api_driver):
        self.api_driver = api_driver

    @allure.step("Send {method} request to {url}")
    def send_api(self, method="GET", url="", params=None):
        """
        Sends an HTTP request with the configured auth headers.

        Args:
            method (str): HTTP method (currently only GET is supported).
            url (str): Target URL.
            params (dict): Optional query string parameters.

        Returns:
            Response: The requests.Response object.
        """
        if method == "GET":
            response = requests.get(url, headers=self.api_driver.HEADERS, params=params)
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            return response
        # TODO: implement remaining HTTP methods
