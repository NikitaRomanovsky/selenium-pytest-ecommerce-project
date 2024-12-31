# Selenium Python Project

## Description
This project is a Selenium-based automation framework designed for testing a WordPress-based eCommerce site. The tests cover various scenarios, including login functionalities, checkout processes, and order verification.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- MySQL
- Chrome WebDriver / Firefox WebDriver

## Structure Overview
1. **Helpers**: 
   - **config_helper**: Provides methods to retrieve configuration such as base URLs and database credentials.
   - **database_helper**: Handles database interactions, such as fetching order information.
   - **generic_helper**: Contains utility functions like generating random emails.

2. **Pages**: 
   - Page Object Model (POM) is implemented using separate classes for each page with dedicated locators and methods.
   - Example: `MyAccountSignedOut` page class provides methods for interacting with the "My Account" page when signed out.

3. **Locators**: 
   - Separate locator classes for each page, holding web element locators.

4. **SeleniumExtended**: 
   - Custom utility class providing enhanced Selenium WebDriver interactions, such as retries, timeouts, and custom waiting conditions.

5. **Tests**: 
   - Organized tests into separate folders following the Page Object Model.
   - Each test class focuses on a specific feature or scenario (e.g., `TestInvalidLogin` for login-related scenarios).
   
6. **Conftest**: 
   - Configurations for managing browser setup, driver initialization, and capturing screenshots on test failure.

## General Practices
- Page Object Model (POM) structure is used, with all page-specific functions stored in dedicated classes.
- All locators are organized in separate locator files specific to each page.
- Tests are organized in folders based on the feature or functionality they test.
- Helper functions assist with common tasks such as generating random emails and interacting with the database.
- HTML reports and screenshots are captured for failed tests to aid debugging.
