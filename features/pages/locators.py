from selenium.webdriver.common.by import By

class Locators:

    LOGIN_PAGE = (By.XPATH, "//div[text()='Swag Labs']")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    HOME_PAGE = (By.XPATH, "//span[text()='Products']")