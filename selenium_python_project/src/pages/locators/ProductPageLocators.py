from selenium.webdriver.common.by import By


class ProductPageLocators:

    COLOR_DROPDOWN_BUTTON = (By.ID, "pa_color")
    LOGO_DROPDOWN_BUTTON = (By.ID, "logo")
    CLEAR_BUTTON = (By.CSS_SELECTOR, ".reset_variations")
