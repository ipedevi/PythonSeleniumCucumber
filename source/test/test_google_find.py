# source/test/test_google_find.py
from page_objects.google_page import google_page_object
from framework.base_test import BaseTest

class TestGoogleFind(BaseTest):

    def test_login_google(self):

        assert "Google" in self.driver.title # not needed only to check if the initial page is opened

        google_page = google_page_object(self.driver)

        # Accept cookies
        google_page.accept_cookies()

        # Send text to find
        google_page.find_text_in_google("pytest selenium")

        # Wait and verify the text found
        assert "pytest selenium" in self.driver.title