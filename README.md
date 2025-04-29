# DemoQA Test Automation Framework

This project provides a basic example of a test automation framework using Python, Selenium, and Pytest to test functionalities on the DemoQA website (https://demoqa.com/).

## Description

The framework demonstrates common practices in test automation, including:

- **Page Object Model (POM):** Test logic is separated from page interactions by using page classes (`pages/`).
- **Data-Driven Testing:** Test data (like credentials and search terms) is managed externally in a JSON file (`data/test_data.json`).
- **Cross-Browser Testing:** Easily run tests against different browsers (Chrome, Firefox, Edge) using command-line arguments.
- **Automatic WebDriver Management:** Uses `webdriver-manager` to automatically download and manage the necessary browser drivers.
- **Test Execution with Pytest:** Leverages the Pytest framework for test discovery, execution, reporting, and fixtures.

Currently, the framework includes tests for:

- Login and Logout functionality.
- Searching for books in the Book Store section.

## Features

- Tests DemoQA Login/Logout.
- Tests DemoQA Book Store search.
- Page Object Model implementation.
- JSON-based test data management.
- Supports Chrome, Firefox, and Edge browsers.
- Automatic driver downloads via `webdriver-manager`.
- Test execution powered by `pytest`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python:** Version 3.8 or higher recommended. ([Download Python](https://www.python.org/downloads/))
- **pip:** Python package installer (usually comes with Python).
- **Git:** For cloning the repository. ([Download Git](https://git-scm.com/downloads))
- **Installed Web Browsers:** Have Google Chrome, Mozilla Firefox, or Microsoft Edge installed on your system, depending on which browser you intend to test against.

## Installation and Setup

Follow these steps to set up the project environment:

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url> # Replace <your-repository-url> with the actual URL
    cd <project-directory-name>     # Navigate into the cloned project directory
    ```

2.  **(Recommended) Create and activate a virtual environment:**

    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      `bash
    python3 -m venv venv
    source venv/bin/activate
    `
      _(Using a virtual environment keeps project dependencies isolated.)_

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This command reads the `requirements.txt` file and installs all the necessary Python libraries.

## Running Tests

You can run the automated tests using the Pytest command-line interface. Make sure your virtual environment is activated.

- **Run all tests** (uses Chrome by default):

  ```bash
  pytest
  ```

  or

  ```bash
  python -m pytest
  ```

- **Run tests on a specific browser:**

  ```bash
  pytest --browser firefox
  ```

  ```bash
  pytest --browser edge
  ```

- **Run tests with verbose output:**

  ```bash
  pytest -v
  ```

- **Run tests showing print statements:**

  ```bash
  pytest -s
  ```

- **Run a specific test file:**
  ```bash
  pytest tests/test_login.py
  ```
  ```bash
  pytest tests/test_book_search.py
  ```

## Project Structure

selenium_project/
├── conftest.py # Shared pytest fixtures (driver setup, data loading)
├── data/
│ └── test_data.json # Centralized test data (credentials, keywords)
├── drivers/
│ └── webdriver_factory.py # Creates WebDriver instances for different browsers
├── pages/
│ ├── base_page.py # Base class with common Selenium actions
│ ├── book_store_page.py # Page Object for the Book Store page
│ └── login_page.py # Page Object for the Login page
├── tests/
│ ├── test_book_search.py # Test cases for book searching
│ └── test_login.py # Test cases for login/logout
├── utils/
│ └── data_loader.py # Utility function to load JSON data
├── requirements.txt # Project dependencies
├── pytest.ini # Pytest configuration (optional)
└── README.md # This file

## Tools and Libraries Used

- **Selenium:** Browser automation library.
- **Pytest:** Testing framework for Python.
- **webdriver-manager:** Handles automatic management of browser drivers.
