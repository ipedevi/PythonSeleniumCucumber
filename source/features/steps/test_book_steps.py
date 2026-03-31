import allure
from behave import given, when, then, step


@given("I am on the home page")
@allure.step("Verify the home page has loaded")
def step_on_home_page(context):
    assert "Space" in context.driver.title


@when('I book a trip to "{destination}"')
@allure.step("Click the BOOK button for '{destination}'")
def step_book_destination(context, destination):
    context.last_booked_destination = destination
    context.book_page.click_book_for_planet(destination)


@then("I should see the trip price")
@allure.step("Verify a trip price is displayed on the confirmation page")
def step_verify_trip_price(context):
    assert context.book_page.is_price_displayed()


@then("Valencia should not be available as a destination")
@allure.step("Verify there is no BOOK button for Valencia")
def step_verify_valencia_not_available(context):
    assert not context.book_page.is_destination_available("Valencia")


# --- Checkout form steps (book.feature scenarios 2-4) ---

@when('the user enters "{value}" in the Name field')
@allure.step("Enter '{value}' in the Name field")
def step_enter_name(context, value):
    context.checkout_page.fill_name(value)


@when('the user enters "{value}" in the Email Address field')
@allure.step("Enter '{value}' in the Email Address field")
def step_enter_email(context, value):
    context.checkout_page.fill_email(value)


@when('the user enters "{value}" in the Social Security Number field')
@allure.step("Enter '{value}' in the Social Security Number field")
def step_enter_ssn(context, value):
    context.checkout_page.fill_ssn(value)


@when('the user enters "{value}" in the Phone Number field')
@allure.step("Enter '{value}' in the Phone Number field")
def step_enter_phone(context, value):
    context.checkout_page.fill_phone(value)


@allure.step("Check the terms and conditions checkbox")
@when(u'the user checks the "I agree to the terms and conditions" checkbox')
def step_impl(context):
    context.checkout_page.check_terms()


@when('the user clicks "{button}"')
@allure.step("Click the '{button}' button")
def step_click_button(context, button):
    context.checkout_page.click_button(button)


@then("the booking is completed successfully")
@allure.step("Verify booking confirmation is displayed")
def step_booking_completed(context):
    assert context.checkout_page.is_booking_completed()


@when("the user fills in all required fields")
@allure.step("Fill all required checkout fields")
def step_fill_required_fields(context):
    context.checkout_page.fill_all_required_fields()


@step('the user does not check the "{checkbox}" checkbox')
@allure.step("Skip checking the terms and conditions checkbox")
def step_skip_checkbox(context):
    pass  # Intentionally do nothing


@then('the "{button}" button is disabled')
@allure.step("Verify the '{button}' button is disabled")
def step_button_is_disabled(context, button):
    assert context.checkout_page.is_button_disabled(button)


@when('the user navigates back to "{url}"')
@allure.step("Navigate back to {url}")
def step_navigate_back(context, url):
    context.driver.get(url)


@then('the button on the "{destination}" card displays "{text}"')
@allure.step("Verify the button on the '{destination}' card displays '{text}'")
def step_card_button_text(context, destination, text):
    from selenium.webdriver.common.by import By
    xpath = f"//div[contains(@data-react-toolbox,'card')]//h5[contains(text(),'{destination}')]/../../../div/button"
    button = context.checkout_page.wait_for_element((By.XPATH, xpath))
    assert button.text.strip() == text, f"Expected '{text}', but got '{button.text.strip()}'"
