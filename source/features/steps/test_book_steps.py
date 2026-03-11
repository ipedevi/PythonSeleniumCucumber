import allure
from behave import given, when, then


@given("I am on the home page")
def step_on_home_page(context):
    with allure.step("Verify the home page has loaded"):
        assert "Space" in context.driver.title


@when("I book a trip to Sant Cugat Del Valles")
def step_book_sant_cugat(context):
    with allure.step("Click the BOOK button for Sant Cugat Del Valles"):
        context.book_page.click_book_for_planet("Sant Cugat Del Valles")


@then("I should see the trip price")
def step_verify_trip_price(context):
    with allure.step("Verify a trip price is displayed on the confirmation page"):
        assert context.book_page.is_price_displayed()


@then("Valencia should not be available as a destination")
def step_verify_valencia_not_available(context):
    with allure.step("Verify there is no BOOK button for Valencia"):
        assert not context.book_page.is_destination_available("Valencia")
