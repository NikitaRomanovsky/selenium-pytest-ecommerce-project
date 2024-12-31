from selenium_python_project.src.pages.locators.CheckoutPageLocators import (
    CheckoutPageLocators,
)
from selenium_python_project.src.SeleniumExtended import SeleniumExtended
from selenium_python_project.src.helpers.generic_helpers import generate_random_email


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def input_contact_email_address(self, email_address):
        self.selenium.wait_and_input_text(self.EMAIL_INPUT, email_address)

    def input_billing_first_name(self, first_name):
        self.selenium.wait_and_input_text(self.FIRST_NAME_INPUT, first_name)

    def input_billing_last_name(self, last_name):
        self.selenium.wait_and_input_text(self.LAST_NAME_INPUT, last_name)

    def input_billing_address(self, address):
        self.selenium.wait_and_input_text(self.ADDRESS_INPUT, address)

    def input_billing_city(self, city):
        self.selenium.wait_and_input_text(self.CITY_INPUT, city)

    def input_billing_state_county(self, state_county):
        self.selenium.wait_and_input_text(self.STATE_COUNTY_INPUT, state_county)

    def input_billing_postal_code(self, postal_code):
        self.selenium.wait_and_input_text(self.POSTAL_CODE_INPUT, postal_code)

    def fill_in_billing_info(
        self,
        email_address=None,
        first_name="TestFname",
        last_name="TestLname",
        address="test iela 123",
        city="Riga",
        state_county="Vidzeme",
        postal_code="LV-0000",
    ):
        if not email_address:
            email_address = generate_random_email()

        self.input_contact_email_address(email_address)
        self.input_billing_first_name(first_name)
        self.input_billing_last_name(last_name)
        self.input_billing_address(address)
        self.input_billing_city(city)
        self.input_billing_state_county(state_county)
        self.input_billing_postal_code(postal_code)

    def click_on_place_order_button(self):
        self.selenium.wait_and_click(self.PLACE_ORDER_BUTTON)
