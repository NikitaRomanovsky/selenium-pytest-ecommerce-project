import pytest
import pytest_html
from pathlib import Path
from selenium import webdriver
import os


@pytest.fixture(scope="class")
def initialize_driver(request):
    supported_browsers = ["chrome", "ch", "headlesschrome", "firefox", "ff"]
    browser = os.environ.get("BROWSER", None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(
            f"Provided browser '{browser}' is not one of the supported."
            f"Supported are: {supported_browsers}"
        )

    if browser in ("chrome", "ch", "headlesschrome"):
        driver = webdriver.Chrome()
    elif browser in ("firefox", "ff"):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = (
                True if "initialize_driver" in item.fixturenames else False
            )
            if is_frontend_test:
                report_dir = Path(
                    "/Users/nikitaromanovskis/selenium-python-project/selenium_python_project/report"
                )
                report_dir.mkdir(parents=True, exist_ok=True)

                screenshot_name = f"{item.name}.png"
                screenshot_path = report_dir / screenshot_name

                driver_fixture = item.funcargs["request"].cls.driver
                driver_fixture.save_screenshot(str(screenshot_path))

                extras.append(pytest_html.extras.image(str(screenshot_path)))
        report.extras = extras
