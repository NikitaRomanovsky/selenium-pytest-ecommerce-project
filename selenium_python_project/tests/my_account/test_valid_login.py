import pytest
from selenium_python_project.src.pages.MyAccountSignedOut import MyAccountSignedOut
from selenium_python_project.src.pages.MyAccountSignedIn import MyAccountSignedIn
from selenium_python_project.src.helpers.api_helpers import create_user


@pytest.mark.usefixtures("initialize_driver")
class TestValidLogin:
    email, password = create_user()
    username = email.split("@")[0]
    greeting_text = f"Hello {username} (not {username}? Log out)"

    @pytest.mark.tcid15
    def test_login_with_valid_credentials(self):
        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)

        my_account_out.go_to_my_account()
        my_account_out.input_login_username_or_email(self.email)
        my_account_out.input_login_password(self.password)
        my_account_out.click_login_button()

        my_account_in.verify_user_is_signed_in(self.greeting_text)
