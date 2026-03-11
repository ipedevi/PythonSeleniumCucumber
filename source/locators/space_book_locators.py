from selenium.webdriver.common.by import By


class SpaceBookLocators:
    # BOOK button on a planet card — planet name is injected dynamically in the page object
    BOOK_BUTTON_BY_PLANET = "//h5[contains(text(),'{planet}')]/../../..//button"

    # Element showing the trip price after a successful booking
    TRIP_PRICE = (By.XPATH, "//div/strong[contains(text(),'$')]") 
