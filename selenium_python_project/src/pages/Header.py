from selenium_python_project.src.pages.locators.HeaderLocators import HeaderLocators
from selenium_python_project.src.SeleniumExtended import SeleniumExtended


class Header(HeaderLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def wait_until_cart_item_count_is_updated(self, count):
        expected_text = f"{str(count)} item"
        self.selenium.wait_until_element_contains_text(self.CART_SUMMARY, expected_text)

    def click_on_cart_summary(self):
        self.selenium.wait_and_click(self.CART_SUMMARY)
