from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)
import time


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None, retries=3):
        timeout = timeout if timeout else self.default_timeout
        for _ in range(retries):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator),
                    EC.element_to_be_clickable(locator),
                )
                element.click()
                return
            except (
                TimeoutException,
                StaleElementReferenceException,
                ElementClickInterceptedException,
            ):
                print("Click attempt failed. Retrying...")
                time.sleep(1)
        raise TimeoutException(
            f"Element {locator} not clickable after {retries} retries."
        )

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = (
            err
            if err
            else f"Unable to find elements located by '{locator}',"
            f"after timeout of {timeout}"
        )
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

    def wait_and_get_element_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element_text = (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(locator))
            .text
        )
        return element_text
