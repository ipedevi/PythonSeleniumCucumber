# PythonSeleniumCucumber

Hybrid test automation framework combining BDD (Behave/Cucumber), Selenium WebDriver for UI tests, and Python Requests for API tests. Supports parallel execution via BehaveX and visual reporting via Allure.

---

## Architecture

```
PythonSeleniumCucumber/
├── myconfig.py                  # Project configuration (browser, URLs, API credentials)
├── behave.ini                   # Behave + BehaveX settings (formatter, parallel, logging)
└── source/
    ├── features/                # Gherkin feature files
    │   ├── steps/               # Step definitions
    │   │   ├── test_steps.py    # Web UI steps
    │   │   ├── test_api_steps.py
    │   │   └── test_book_steps.py
    │   └── environment.py       # Behave hooks (driver init/teardown per scenario)
    ├── framework/               # Core framework classes
    │   ├── base_test.py         # WebSession: start_driver / close_driver
    │   ├── base_api_test.py     # ApiDriver: API auth headers setup
    │   ├── base_page.py         # BasePage: wait_for_element (WebDriverWait)
    │   └── base_api_page.py     # BaseApiPage: generic send_api
    ├── page_objects/            # Page Object Model
    │   ├── space_page.py
    │   ├── space_login_page.py
    │   ├── space_book_page.py
    │   └── dog_api_page.py
    └── locators/                # Locators and endpoints separated from page objects
        ├── space_locators.py
        ├── space_login_locators.py
        ├── space_book_locators.py
        └── dog_api_locators.py
```

---

## Key design decisions

- **Web by default**: scenarios run as web (Selenium) unless tagged `@api`.
- **Locators as tuples**: each locator is a `(By.STRATEGY, "value")` tuple stored in a dedicated locators file, consumed with `find_element(*locator)`.
- **Stable waits**: `wait_for_element` uses `WebDriverWait` + `expected_conditions.element_to_be_clickable`, handling `StaleElementReferenceException` automatically.
- **Local or remote execution**: set `browser` in `myconfig.py` to `chrome_local`, `firefox_local`, `chrome_remote` or `firefox_remote`. Remote targets a Selenium Grid.
- **Parallel-safe**: each scenario creates and destroys its own driver instance — no shared state between workers.
- **Allure steps**: `@allure.step` on every page object method and `with allure.step()` in every step definition for full traceability in the report.
- **Screenshots**: attached to the Allure report at the end of every scenario, plus an extra one labeled "Failure screenshot" on failures.

---

## Install

```bash
pip install selenium behavex allure-behave requests
```

Allure CLI (to serve reports):
```bash
brew install allure       # macOS
```

---

## Configuration

Edit `myconfig.py` at the project root:

```python
SELENIUM_CONFIG = {
    "browser": "chrome_local",    # "chrome_local", "firefox_local", "chrome_remote", "firefox_remote"
    "headless": False,            # True for headless mode (local only)
    "initial_page": "https://demo.testim.io/",
    "remote_url": "http://<grid-host>:4444/wd/hub"  # used when browser is *_remote
}

API_CONFIG = {
    "apikey": ""   # API key sent as x-api-key header
}
```

---

## Tagging

| Tag | Behaviour |
|-----|-----------|
| *(none)* | Web (Selenium) — default |
| `@api` | API test (Requests) |

---

## Execution

```bash
# Run all tests — sequential
behavex source/features

# Run all tests — parallel by scenario (recommended)
behavex source/features --parallel-scheme scenario --parallel-processes 4

# Run all tests — parallel by feature file
behavex source/features --parallel-scheme feature --parallel-processes 4

# Filter by tag
behavex source/features --tags=@api

# View Allure report after any execution
allure serve allure-results
```

| Option | Values | Description |
|---|---|---|
| `--parallel-scheme` | `scenario` / `feature` | Unit of parallelism. `scenario` = max granularity |
| `--parallel-processes` | integer | Number of concurrent workers |
| `--tags` | `@tag` / `~@tag` | Include or exclude scenarios by tag |
