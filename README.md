# Selenium Python Project

## Description
This project is a Selenium-based automation framework designed for testing a WordPress-based eCommerce site. The tests cover various scenarios, including login functionalities, checkout processes, order verification and product details configuration. The eCommerce site and its BackEnd (DB and API) run locally.

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
   - **api_helper**: Handles API interactions, such as creating new user.

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
- Helper functions assist with common tasks such as generating random emails, interacting with the database and sending API requests.
- HTML reports and screenshots are captured for failed tests to aid debugging.

## How my website looks like:

<img width="600" alt="Screenshot 2024-12-31 at 13 35 39" src="https://github.com/user-attachments/assets/89b1a099-bf60-4262-997d-d5120358d13e" />

<img width="600" alt="Screenshot 2024-12-31 at 13 35 55" src="https://github.com/user-attachments/assets/ebb25699-42d0-4746-961b-41924520bfb4" />

<img width="600" alt="Screenshot 2024-12-31 at 13 35 29" src="https://github.com/user-attachments/assets/f10180c7-8044-42cc-b3f1-fff5a9239e70" />

## How my HTML report looks like:

<img width="600" alt="Screenshot 2024-12-31 at 13 40 36" src="https://github.com/user-attachments/assets/983da0c4-49cb-480a-b325-5895eea77e44" />
