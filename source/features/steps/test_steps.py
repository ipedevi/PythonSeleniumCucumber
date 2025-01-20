from behave import given, when, then

@given("I visit the login page")
def step_visit_login_page(context):
    context.space_page.click_login_button()

@when("I enter next valid credentials {user} amd {psw}")
def step_enter_credentials(context, user, psw):
    context.login_page.add_username(user)
    context.login_page.add_password(psw)
    context.login_page.click_login_button()

@then("I should see the dashboard")
def step_verify_dashboard(context):
    assert not context.space_page.is_login_button_displayed()

@given("I visit the home page")
def step_visit_home_page(context):
    assert "Space" in context.driver.title

@then("I should see the home page")
def step_verify_home_page(context):
    assert context.space_page.is_login_button_displayed()