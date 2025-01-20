import sys
import os

# Add root project directory (source) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from framework.base_test import BaseTest
from page_objects.space_page import space_page_object
from page_objects.space_login_page import space_login_page_object


def before_all(context):
    # Start test environment
    print("Starting Selenium, Pytest, Behave tests...")


def before_scenario(context, scenario):
    # Configuring object before scenario
    print(f"Starting scenario driver for: {scenario.name}")
    context.base_test = BaseTest()  # Creating BaseTest instance
    context.driver = BaseTest.start_selenium_driver()  # Initializing the driver
    context.base_test.driver = context.driver  # Assigning driver to object base_test
    # Initializing page objects
    context.space_page = space_page_object(context.driver)
    context.login_page = space_login_page_object(context.driver)


def after_scenario(context, scenario):
    # Closing driver after scenario
    print(f"Closing scenario driver for: {scenario.name}")
    BaseTest.quit_selenium_driver(context.driver)


def after_all(context):
    # Closing tests
    print("Finalizing Selenium, Pytest, Behave tests...")