from selenium_python_project.src.pages.locators.MyAccountSignedInLocators import (
    MyAccountSignedInLocators,
)
from selenium_python_project.src.SeleniumExtended import SeleniumExtended


class MyAccountSignedIn(MyAccountSignedInLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.selenium.wait_until_element_is_visible(self.NAVIGATION_PANEL_LOGOUT_BUTTON)
