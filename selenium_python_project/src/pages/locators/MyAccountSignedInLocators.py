from selenium.webdriver.common.by import By


class MyAccountSignedInLocators:

    NAVIGATION_PANEL_LOGOUT_BUTTON = (
        By.CSS_SELECTOR,
        ".woocommerce-MyAccount-navigation-link--customer-logout",
    )