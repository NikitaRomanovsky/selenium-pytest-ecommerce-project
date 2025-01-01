import pytest
import random
import time
from selenium_python_project.src.pages.ProductPage import ProductPage


@pytest.mark.usefixtures("initialize_driver")
class TestProductOptions:

    default_dropdown_choice = "Choose an option"
    color_to_choose = random.choice(["Blue", "Green", "Red"])
    logo_choice = random.choice(["Yes", "No"])

    @pytest.mark.tcid100
    def test_select_color_and_clear_choice(self):

        product_page = ProductPage(self.driver)

        product_page.go_to_product_page()
        product_page.select_color_option_and_verify(self.color_to_choose)
        product_page.click_clear_button()
        product_page.verify_user_choice_is_cleared(
            "color", self.default_dropdown_choice
        )

    @pytest.mark.tcid101
    def test_select_logo_and_clear_choice(self):

        product_page = ProductPage(self.driver)

        product_page.go_to_product_page()
        product_page.select_logo_option_and_verify(self.logo_choice)
        product_page.click_clear_button()
        product_page.verify_user_choice_is_cleared("logo", self.default_dropdown_choice)
