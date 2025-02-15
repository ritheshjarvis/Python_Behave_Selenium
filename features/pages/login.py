from features.pages.locators import Locators


class Login:

    def __init__(self, driver):
        self.driver = driver

    def verify_login_page(self):
        login_page_element = self.driver.find_element(*Locators.LOGIN_PAGE)
        assert login_page_element.is_displayed(), 'Login page is not displayed'

    def enter_username(self, username):
        username_element = self.driver.find_element(*Locators.USERNAME_FIELD)
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.driver.find_element(*Locators.PASSWORD_FIELD)
        password_element.send_keys(password)

    def click_login(self):
        login_element = self.driver.find_element(*Locators.LOGIN_BUTTON)
        login_element.click()