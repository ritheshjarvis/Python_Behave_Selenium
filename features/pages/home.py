from features.pages.locators import Locators


class Home:

    def __init__(self, driver):
        self.driver = driver

    def verify_home_page(self):
        home_page_element = self.driver.find_element(*Locators.HOME_PAGE)
        assert home_page_element.is_displayed(), 'Home page is displayed'