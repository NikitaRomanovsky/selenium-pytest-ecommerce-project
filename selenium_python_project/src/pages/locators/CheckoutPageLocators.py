from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    EMAIL_INPUT = (By.ID, "email")

    COUNTRY_DROPDOWN = (By.ID, "billing-country")

    FIRST_NAME_INPUT = (By.ID, "billing-first_name")

    LAST_NAME_INPUT = (By.ID, "billing-last_name")

    ADDRESS_INPUT = (By.ID, "billing-address_1")

    ADDITIONAL_ADDRESS_INFO_INPUT = (By.ID, "billing-address_2")

    CITY_INPUT = (By.ID, "billing-city")

    STATE_COUNTY_INPUT = (By.ID, "billing-state")

    POSTAL_CODE_INPUT = (By.ID, "billing-postcode")

    PHONE_INPUT = (By.ID, "billing-phone")

    PLACE_ORDER_BUTTON = (
        By.CSS_SELECTOR,
        'button[class*="wc-block-components-checkout-place-order-button"]',
    )
