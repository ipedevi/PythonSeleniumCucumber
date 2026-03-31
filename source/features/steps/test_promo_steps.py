import allure
import myconfig
from behave import given, then, when


@given('the Order Summary shows the full price "{price}"')
@allure.step("Verify Order Summary displays full price {price}")
def step_verify_full_price(context, price):
    actual = context.checkout_page.get_order_total()
    assert actual == price, f"Expected price '{price}', but got '{actual}'"


@when('the user enters the promo code in the "{field}" field')
@allure.step("Enter promo code in the '{field}' field")
def step_enter_promo_code(context, field):
    promo_code = myconfig.PROMO_CONFIG.get("code", "PROMO")
    context.checkout_page.fill_promo_code(promo_code)


@then('the price updates to the discounted price "{price}"')
@allure.step("Verify price updated to discounted price {price}")
def step_verify_discounted_price(context, price):
    actual = context.checkout_page.get_order_total()
    assert actual == price, f"Expected discounted price '{price}', but got '{actual}'"

@when('the user clicks APPLY button')
@allure.step("<the user clicks APPLY button")
def step_click_apply_promo_code(context):
    context.checkout_page.click_apply_button()
    
