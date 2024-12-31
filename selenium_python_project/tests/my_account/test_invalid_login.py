import pytest
from selenium_python_project.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("initialize_driver")
class TestInvalidLogin:
    non_existing_username = "nonExisting"
    non_existing_email = "nonexistingemail@gmail.com"
    admin_username = "admin"

    expected_error_message_username = f"Error: The username {non_existing_username} is not registered on this site. If you are unsure of your username, try your email address instead."
    expected_error_message_email = (
        "Unknown email address. Check again or try your username."
    )
    expected_error_message_password = f"Error: The password you entered for the username {admin_username} is incorrect. Lost your password?"

    @pytest.mark.tcid10
    def test_login_with_non_existing_username(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username_or_email(self.non_existing_username)
        my_account.input_login_password("password")
        my_account.click_login_button()
        my_account.wait_until_error_is_displayed(self.expected_error_message_username)

    @pytest.mark.tcid11
    def test_login_with_non_existing_email(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username_or_email(self.non_existing_email)
        my_account.input_login_password("password")
        my_account.click_login_button()
        my_account.wait_until_error_is_displayed(self.expected_error_message_email)

    @pytest.mark.tcid12
    def test_login_with_invalid_password(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username_or_email("admin")
        my_account.input_login_password("password")
        my_account.click_login_button()
        my_account.wait_until_error_is_displayed(self.expected_error_message_password)
