import allure
from behave import given, when, then


@given("I visit the login page")
def step_visit_login_page(context):
    with allure.step("Click the login button on the home page to open the login form"):
        context.space_page.click_login_button()


@when("I enter next valid credentials {user} amd {psw}")
def step_enter_credentials(context, user, psw):
    with allure.step(f"Fill in credentials for user '{user}' and submit the form"):
        context.login_page.add_username(user)
        context.login_page.add_password(psw)
        context.login_page.click_login_button()


@then("I should see the dashboard")
def step_verify_dashboard(context):
    with allure.step("Verify the login button is no longer visible (user is logged in)"):
        assert not context.space_page.is_login_button_displayed()


@when("I enter only username {user}")
def step_enter_only_username(context, user):
    with allure.step(f"Fill in only the username '{user}' and submit without password"):
        context.login_page.add_username(user)
        context.login_page.click_login_button()


@when("I enter only password {psw}")
def step_enter_only_password(context, psw):
    with allure.step("Fill in only the password and submit without username"):
        context.login_page.add_password(psw)
        context.login_page.click_login_button()


@then("I should see a missing password error")
def step_verify_password_error(context):
    with allure.step("Verify the missing password error is displayed"):
        assert context.login_page.is_password_error_displayed()


@then("I should see a missing username error")
def step_verify_username_error(context):
    with allure.step("Verify the missing username error is displayed"):
        assert context.login_page.is_username_error_displayed()


@given("I visit the home page")
def step_visit_home_page(context):
    with allure.step("Verify the page title contains 'Space'"):
        assert "Space" in context.driver.title


@then("I should see the home page")
def step_verify_home_page(context):
    with allure.step("Verify the login button is visible on the home page"):
        assert context.space_page.is_login_button_displayed()
