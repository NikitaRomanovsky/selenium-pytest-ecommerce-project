from woocommerce import API
from selenium_python_project.src.helpers.config_helpers import get_api_credentials
from selenium_python_project.src.helpers.generic_helpers import (
    generate_random_password,
    generate_random_email,
)


def create_api_object():
    api_creds = get_api_credentials()

    wcapi = API(
        url=api_creds["base_url"],
        consumer_key=api_creds["api_key"],
        consumer_secret=api_creds["api_secret"],
        version="wc/v3",
    )

    return wcapi


def create_user():
    api_obj = create_api_object()
    email = generate_random_email()
    password = generate_random_password()

    create_customer_payload = {
        "email": email,
        "password": password,
    }
    response = api_obj.post("customers", create_customer_payload)

    assert (
        response.status_code == 201
    ), f"Failed to create user. Response: {response.json()}"

    return email, password
