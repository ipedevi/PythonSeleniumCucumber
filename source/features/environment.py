import sys
import os

# Add source and project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "source")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import allure
from framework.base_test import WebSession
from page_objects.space_page import SpacePageObject
from page_objects.space_login_page import SpaceLoginPageObject
from page_objects.space_book_page import SpaceBookPageObject

from framework.base_api_test import ApiDriver
from page_objects.dog_api_page import DogApiPageObject


def before_scenario(context, scenario):
    if 'api' in context.tags:
        # API scenario: initialize the API driver and page objects
        context.driver = ApiDriver()
        context.dog_api_page = DogApiPageObject(context.driver)
    else:
        # Web scenario (default): initialize browser session and page objects
        context.session = WebSession()
        context.driver = context.session.start_driver()
        context.space_page = SpacePageObject(context.driver)
        context.login_page = SpaceLoginPageObject(context.driver)
        context.book_page = SpaceBookPageObject(context.driver)


def after_scenario(context, scenario):
    if hasattr(context, 'session') and hasattr(context, 'driver'):
        screenshot = context.driver.get_screenshot_as_png()

        # Always attach a screenshot at the end of every scenario
        allure.attach(screenshot, name=f"End of scenario [{scenario.status}]",
                      attachment_type=allure.attachment_type.PNG)

        # Attach an additional screenshot explicitly labeled as failure
        if scenario.status == 'failed':
            allure.attach(screenshot, name="Failure screenshot",
                          attachment_type=allure.attachment_type.PNG)

        context.session.close_driver()


def after_all(context):
    print("Finalizing tests...")
