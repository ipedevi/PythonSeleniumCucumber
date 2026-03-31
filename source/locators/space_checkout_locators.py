from selenium.webdriver.common.by import By


class SpaceCheckoutLocators:
    # Checkout form input fields
    NAME_INPUT = (By.XPATH, "(//div[contains(@class,'CustomerInfo')]/input)[1]")
    EMAIL_INPUT = (By.XPATH, "(//div[contains(@class,'CustomerInfo')]/input)[2]")
    SSN_INPUT = (By.XPATH, "(//div[contains(@class,'CustomerInfo')]/input)[3]")
    PHONE_INPUT = (By.XPATH, "(//div[contains(@class,'CustomerInfo')]/input)[4]")

    # Terms and conditions checkbox
    TERMS_CHECKBOX = (By.XPATH, "//input[contains(@type,'checkbox')]")

    # PAY NOW button
    PAY_NOW_BUTTON = (By.XPATH, "//button[contains(text(),'PAY NOW')]")

    # Booking confirmation indicator (shown after successful payment)
    BOOKING_CONFIRMATION = (By.XPATH, "//*[contains(text(),'Booking') or contains(text(),'booking') or contains(text(),'Thank') or contains(text(),'Success')]")

    # Order total / price on checkout page
    ORDER_TOTAL = (By.XPATH, "//strong[contains(text(),'$')]")

    # Promo code input field
    PROMO_CODE_INPUT = (By.XPATH, "//input[contains(@name,'promo')]")

    # Apply promo code button
    APPLY_BUTTON = (By.XPATH, "//button[contains(@class,'apply-button')]")

    # Generic button by text — use .format(text='...') to build at runtime
    BUTTON_BY_TEXT = "//button[contains(text(),'{text}')]"

    # BOOKED button on a planet card — planet name is injected dynamically
    BOOKED_BUTTON_BY_PLANET = "//h5[contains(text(),'{planet}')]/../../..//button[contains(text(),'BOOKED')]"
