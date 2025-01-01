from selenium_python_project.src.SeleniumExtended import SeleniumExtended
from selenium_python_project.src.pages.locators.CartPageLocators import CartPageLocators
from selenium_python_project.src.configs.generic_configs import GeneralConfigs
from selenium_python_project.src.helpers.config_helpers import get_base_url


class CartPage(CartPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        base_url = get_base_url()
        self.driver.get(f"{base_url}/cart/")

    def get_all_product_names(self):
        product_names_elements = self.selenium.wait_and_get_visible_elements(
            self.PRODUCT_NAMES_IN_CART
        )
        product_names = [i.text for i in product_names_elements]
        return product_names

    def expand_add_coupon_field(self):
        self.selenium.wait_and_click(self.EXPAND_COUPON_INPUT_BUTTON)

    def input_coupon_code(self, code):
        self.selenium.wait_and_input_text(self.COUPON_CODE_INPUT_FIELD, code)

    def click_apply_coupon_code_button(self):
        self.selenium.wait_and_click(self.APPLY_COUPON_CODE_BUTTON)

    def apply_coupon(self, code):
        self.expand_add_coupon_field()
        self.input_coupon_code(code)
        self.click_apply_coupon_code_button()
        pop_up_message = self.get_coupon_applied_pop_up_text()
        assert (
            pop_up_message
            == f'Coupon code "{GeneralConfigs.FREE_COUPON}" has been applied to your cart.',
            f"Unexpected pop-up text when applying coupon.",
        )

    def get_coupon_applied_pop_up_text(self):
        self.selenium.wait_and_get_element_text(self.COUPON_CODE_APPLIED_POP_UP)

    def wait_until_total_amount_is_zero(self):
        self.selenium.wait_until_element_contains_text(
            self.TOTAL_MONEY_AMMOUNT, "0,00 €"
        )

    def click_proceed_to_checkout_button(self):
        self.selenium.wait_and_click(self.PROCEED_TO_CHECKOUT_BUTTON)
