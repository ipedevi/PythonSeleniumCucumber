import allure
from behave import given, when, then


@given("I use thedogapi with my API key")
def step_use_thedogapi(context):
    with allure.step("Verify TheDogApi driver is initialized"):
        assert context.dog_api_page is not None


@when("I request a random image of a dog")
def step_request_random_image(context):
    with allure.step("Send GET request to TheDogApi random image endpoint"):
        context.result = context.dog_api_page.get_random_image()
        allure.attach(
            context.result.text,
            name="TheDogApi response",
            attachment_type=allure.attachment_type.JSON
        )


@then("I should receive a valid response with the image URL")
def step_verify_image_url(context):
    with allure.step("Verify response contains a valid HTTPS image URL"):
        image_url = context.dog_api_page.get_image_url(context.result)
        assert image_url.startswith("https://"), f"Expected HTTPS URL, got: {image_url}"
        allure.attach(
            image_url,
            name="Image URL",
            attachment_type=allure.attachment_type.TEXT
        )
