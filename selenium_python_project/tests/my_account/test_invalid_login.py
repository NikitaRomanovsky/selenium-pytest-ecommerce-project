import pytest
from selenium_python_project.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("initialize_driver")
class TestInvalidLogin:
    non_existing_username = "nonExisting"
    expected_error_message = f"Error: The username {non_existing_username} is not registered on this site. If you are unsure of your username, try your email address instead."

    @pytest.mark.tcid12
    def test_login_with_non_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(self.non_existing_username)
        my_account.input_login_password("password")
        my_account.click_login_button()
        my_account.wait_until_error_is_displayed(self.expected_error_message)
