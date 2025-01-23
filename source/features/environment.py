import sys
import os

# Add root project directory (source) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "source")))

from framework.base_test import prepare_driver
from page_objects.space_page import SpacePageObject
from page_objects.space_login_page import SpaceLoginPageObject

from framework.base_api_test import ApiDriver
from page_objects.marvel_page import MarvelPageObject
from page_objects.marvel_previews_page import MarvelPreviewsPageObject

def before_scenario(context, scenario):
    if 'web' in context.tags:
        print(f"Starting driver for scenario: {scenario.name}")
        try:
            context.driver = prepare_driver()  # Retrieve the initialized driver
            print(f"Driver retrieved in before_scenario: {context.driver}")
            context.space_page = SpacePageObject(context.driver)
            context.login_page = SpaceLoginPageObject(context.driver)
        except RuntimeError as e:
            print(f"Error during WebDriver initialization: {e}")
            raise
    elif 'api' in context.tags:
        try:
            context.driver = ApiDriver()  # Retrieve the initialized driver
            print(f"API Driver retrieved in before_scenario: {context.driver}")
            context.marvel_page = MarvelPageObject(context.driver)
            context.marvel_previews_page = MarvelPreviewsPageObject(context.driver)
        except RuntimeError as e:
            print(f"Error during API Driver initialization: {e}")
            raise


def after_scenario(context, scenario):
    if 'web' in context.tags:
        print(f"Closing driver for scenario: {scenario.name}")
        if hasattr(context, "driver") and context.driver is not None:
            context.driver.quit()


def after_all(context):
    print("Finalizing Selenium tests...")
