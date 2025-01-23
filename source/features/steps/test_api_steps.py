from behave import given, when, then

@given("I visit public marvel api")
def step_visit_login_page(context):
    context.result = context.marvel_page.get_marvel_url()

@when("I obtain the first published title")
def step_verify_dashboard(context):
    context.url = context.marvel_page.get_resource_uri(context.result, 0)

@then("I can obtain deeper info from this title")
def step_verify_home_page(context):
    result = context.marvel_previews_page.get_marvel_previews_url(context.url)
    assert context.marvel_previews_page.get_resource_title(result) == 'Marvel Previews (2017)'