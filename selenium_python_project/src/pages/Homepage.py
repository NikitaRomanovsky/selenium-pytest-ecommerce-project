from selenium_python_project.src.helpers.config_helpers import get_base_url
from selenium_python_project.src.pages.locators.HomepageLocators import HomepageLocators
from selenium_python_project.src.SeleniumExtended import SeleniumExtended


class Homepage(HomepageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        base_url = get_base_url()
        self.driver.get(base_url)

    def add_first_item_to_cart(self):
        self.selenium.wait_and_click(self.FIRST_ADD_TO_CART)
