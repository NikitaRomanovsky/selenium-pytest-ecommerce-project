from selenium.webdriver.support.ui import Select
from selenium_python_project.src.pages.locators.ProductPageLocators import (
    ProductPageLocators,
)
from selenium_python_project.src.SeleniumExtended import SeleniumExtended
from selenium_python_project.src.helpers.config_helpers import get_base_url


class ProductPage(ProductPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_product_page(self):
        base_url = get_base_url()
        self.driver.get(f"{base_url}/product/hoodie/")

    def select_color_option(self, color):
        dropdown = self.selenium.wait_and_get_visible_element(
            self.COLOR_DROPDOWN_BUTTON
        )
        select_color = Select(dropdown)
        select_color.select_by_visible_text(color)

    def get_selected_color_option(self):
        dropdown = self.selenium.wait_and_get_visible_element(
            self.COLOR_DROPDOWN_BUTTON
        )
        selected_color = Select(dropdown)
        return selected_color.first_selected_option.text

    def click_clear_button(self):
        self.selenium.wait_and_click(self.CLEAR_BUTTON)

    def select_logo_option(self, option):
        dropdown = self.selenium.wait_and_get_visible_element(self.LOGO_DROPDOWN_BUTTON)
        select_logo = Select(dropdown)
        select_logo.select_by_visible_text(option)

    def get_selected_logo_option(self):
        dropdown = self.selenium.wait_and_get_visible_element(self.LOGO_DROPDOWN_BUTTON)
        selected_logo = Select(dropdown)
        return selected_logo.first_selected_option.text

    def select_color_option_and_verify(self, color):
        self.select_color_option(color)
        selected_color = self.get_selected_color_option()
        assert (
            selected_color == color
        ), f"Unexpected color got selected, should be {color} but got {selected_color}"

    def select_logo_option_and_verify(self, option):
        self.select_logo_option(option)
        selected_logo = self.get_selected_logo_option()
        assert (
            selected_logo == option
        ), f"Unexpected logo choice got selected, should be {option} but got {selected_logo}"

    def verify_user_choice_is_cleared(self, choice_to_check, default_choice):
        if choice_to_check == "color":
            selected_color = self.get_selected_color_option()
            assert (
                selected_color == default_choice
            ), f"Color choice was not cleared and set to default '{default_choice}', it is still {selected_color}"
        elif choice_to_check == "logo":
            selected_option = self.get_selected_logo_option()
            assert (
                selected_option == default_choice
            ), f"Logo choice was not cleared and set to default '{default_choice}', it is still {selected_option}"
