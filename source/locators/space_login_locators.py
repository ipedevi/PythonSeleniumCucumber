from selenium.webdriver.common.by import By

class SpaceLoginLocators:
    USER_INPUT = (By.XPATH, "id('login')//input[contains(@type, 'text')]")
    PASSWORD_INPUT = (By.XPATH, "id('login')//input[contains(@type, 'password')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@form, 'login')]")
    USERNAME_ERROR = (By.XPATH, "id('login')//span[contains(text(),'Name')][contains(text(),'required')]")
    PASSWORD_ERROR = (By.XPATH, "id('login')//span[contains(text(),'Password')][contains(text(),'required')]") 
