import pytest
from selenium_python_project.src.pages.MyAccountSignedOut import MyAccountSignedOut
from selenium_python_project.src.pages.MyAccountSignedIn import MyAccountSignedIn
from selenium_python_project.src.helpers.generic_helpers import (
    generate_random_email,
    generate_random_password,
)


@pytest.mark.usefixtures("initialize_driver")
class TestRegisterNewUser:
    random_email = generate_random_email()
    random_password = generate_random_password()
    username = random_email.split("@")[0]

    greeting_text = f"Hello {username} (not {username}? Log out)"
    strong_password_helper_text = "Strong"
    very_weak_password_helper_text = "Very weak - Please enter a stronger password."

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)

        my_account_out.go_to_my_account()
        my_account_out.input_register_email(self.random_email)
        my_account_out.input_register_password(self.random_password)
        my_account_out.verify_helper_text_is_present(self.strong_password_helper_text)
        my_account_out.click_register_button()
        my_account_in.verify_user_is_signed_in(self.greeting_text)

    @pytest.mark.tcid14
    def test_register_invalid_new_user(self):
        my_account_out = MyAccountSignedOut(self.driver)

        my_account_out.go_to_my_account()
        my_account_out.input_register_email(self.random_email)
        my_account_out.input_register_password("password")
        my_account_out.verify_helper_text_is_present(
            self.very_weak_password_helper_text
        )
        my_account_out.verify_register_button_is_disabled("disabled")
