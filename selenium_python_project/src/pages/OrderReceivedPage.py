from selenium_python_project.src.pages.locators.OrderReceivedPageLocators import (
    OrderReceivedPageLocators,
)
from selenium_python_project.src.SeleniumExtended import SeleniumExtended


class OrderReceivedPage(OrderReceivedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.selenium.wait_until_element_contains_text(
            self.ORDER_RECEIVED_HEADER, "Order received"
        )

    def get_order_number(self):
        return self.selenium.wait_and_get_element_text(self.ORDER_NUMBER)
