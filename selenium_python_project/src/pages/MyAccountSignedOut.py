from selenium_python_project.src.pages.locators.MyAccountSignedOutLocators import (
    MyAccountSignedOutLocators,
)
from selenium_python_project.src.helpers.config_helpers import get_base_url
from selenium_python_project.src.SeleniumExtended import SeleniumExtended


class MyAccountSignedOut(MyAccountSignedOutLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        self.driver.get(f"{base_url}/my-account/")

    def input_login_username(self, username):
        self.selenium.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.selenium.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.selenium.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, error):
        self.selenium.wait_until_element_contains_text(self.ERRORS_UL, error)

    def input_register_email(self, email):
        self.selenium.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.selenium.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.selenium.wait_and_click(self.REGISTER_BUTTON)
