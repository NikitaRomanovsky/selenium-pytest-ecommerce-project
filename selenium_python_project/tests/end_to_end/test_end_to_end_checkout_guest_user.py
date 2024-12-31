import pytest
from selenium_python_project.src.pages.Homepage import Homepage
from selenium_python_project.src.pages.Header import Header
from selenium_python_project.src.pages.CartPage import CartPage
from selenium_python_project.src.pages.CheckoutPage import CheckoutPage
from selenium_python_project.src.pages.OrderReceivedPage import OrderReceivedPage
from selenium_python_project.src.configs.generic_configs import GeneralConfigs
from selenium_python_project.src.helpers.database_helpers import (
    get_order_from_db_by_order_id,
)
import time


@pytest.mark.usefixtures("initialize_driver")
class TestEndToEndCheckoutGuestUser:
    coupon_code = GeneralConfigs.FREE_COUPON

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        homepage = Homepage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_received_page = OrderReceivedPage(self.driver)

        homepage.go_to_homepage()
        homepage.add_first_item_to_cart()

        header.wait_until_cart_item_count_is_updated(1)
        header.click_on_cart_summary()

        product_names = cart_page.get_all_product_names()
        assert (
            len(product_names) == 1
        ), f"Expected 1 item in cart but got {len(product_names)}"
        cart_page.apply_coupon(self.coupon_code)
        cart_page.wait_until_total_amount_is_zero()
        cart_page.click_proceed_to_checkout_button()

        checkout_page.fill_in_billing_info()
        checkout_page.click_on_place_order_button()

        order_received_page.verify_order_received_page_loaded()
        order_id = order_received_page.get_order_number()

        db_order = get_order_from_db_by_order_id(order_id)
        assert db_order, (
            f"After creating order with FE, not found in DB." f"Order ID is: {order_id}"
        )
