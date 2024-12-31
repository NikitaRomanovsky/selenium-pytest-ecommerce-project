import pytest
from selenium_python_project.src.pages.MyAccountSignedOut import MyAccountSignedOut
from selenium_python_project.src.pages.MyAccountSignedIn import MyAccountSignedIn
from selenium_python_project.src.helpers.generic_helpers import generate_random_email


@pytest.mark.usefixtures("initialize_driver")
class TestRegisterNewUser:
    random_email = generate_random_email()

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)

        my_account_out.go_to_my_account()
        my_account_out.input_register_email(self.random_email)
        my_account_out.input_register_password("ThisIsMyPassword12345@")
        my_account_out.click_register_button()

        my_account_in.verify_user_is_signed_in()
