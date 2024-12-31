from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:

    ORDER_RECEIVED_HEADER = (By.CSS_SELECTOR, ".entry-title")

    ORDER_NUMBER = (By.CSS_SELECTOR, "li.order strong")
