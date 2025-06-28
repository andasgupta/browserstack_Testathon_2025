# Kolkata BugBash BDD Test Framework

A comprehensive BDD testing framework for the Kolkata BugBash application using pytest-bdd, Selenium, and BrowserStack integration with Page Object Model architecture.

## 🚀 Framework Features

- **BDD Testing**: Gherkin-based scenarios with pytest-bdd
- **Page Object Model**: Maintainable and scalable test architecture
- **Cross-Browser Testing**: BrowserStack integration for multiple platforms
- **Data-Driven Testing**: Scenario Outlines with Examples tables
- **End-to-End Testing**: Complete user journey automation
- **Bug Verification**: Automated testing of known issues
- **Comprehensive Reporting**: HTML reports with screenshots

## 📋 Test Coverage

### Login Functionality
- ✅ Valid login with demo credentials
- ✅ Invalid password validation
- ✅ Invalid username validation
- ✅ Error message verification

### E-Commerce Flow
- ✅ Product browsing and selection
- ✅ Add to cart functionality
- ✅ Cart quantity management
- ✅ Price calculations
- ✅ Checkout process
- ✅ Order confirmation
- ✅ Shipping form validation

### Bug Testing
- 🐛 Galaxy S20 Ultra cart issue (product doesn't add to cart)
- 🐛 Download receipt functionality failure
- ✅ Cart management edge cases

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+
- BrowserStack account

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd browserstack_Testathon_2025
   ```

2. **Install dependencies:**
   ```bash
   # Using full Python path (Windows)
   C:\Python311\python.exe -m pip install --user -r requirements.txt
   
   # Or using pip directly
   pip install -r requirements.txt
   ```

3. **Set BrowserStack credentials:**
   ```bash
   # Windows
   setx BROWSERSTACK_USERNAME "anikdasgupta_sW03Uz"
   setx BROWSERSTACK_ACCESS_KEY "gFspSApHHEnMSwGzeHk8"
   
   # Or set in current session
   set BROWSERSTACK_USERNAME=anikdasgupta_sW03Uz
   set BROWSERSTACK_ACCESS_KEY=gFspSApHHEnMSwGzeHk8
   ```

## 🏃‍♂️ Running Tests

### Basic Execution
```bash
# Run all tests
C:\Python311\python.exe -m pytest tests/step_defs/ -v

# Run with specific platform
C:\Python311\python.exe -m pytest tests/step_defs/ --platform=0 -v

# Run E2E tests only
C:\Python311\python.exe -m pytest tests/features/e2e/ -v
```

### Platform Options
- `--platform=0` - Windows 10 Chrome 120.0
- `--platform=1` - macOS Monterey Safari 15.6
- `--platform=2` - iPhone 13 Chromium

### Batch Scripts
```bash
# Quick test execution
run_tests_direct.bat
```

## 📁 Project Structure

```
browserstack_Testathon_2025/
├── pages/                          # Page Object Model
│   ├── base_page.py               # Base page with common methods
│   ├── login_page.py               # Login page objects
│   ├── product_page.py             # Product and cart page objects
│   └── checkout_page.py            # Checkout and order page objects
├── tests/
│   ├── features/                   # BDD Feature files
│   │   ├── sample_test.feature     # Main test scenarios
│   │   └── e2e/
│   │       └── shopping_flow.feature # E2E scenarios
│   └── step_defs/                  # Step definitions
│       └── test_sample_steps.py    # Implementation of steps
├── utils/
│   └── browserstack_driver.py      # BrowserStack WebDriver utility
├── reports/                        # Test execution reports
├── browserstack.yml               # BrowserStack configuration
├── conftest.py                    # pytest fixtures and hooks
├── pytest.ini                    # pytest configuration
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 📝 Writing New Tests

### 1. Create Feature File
```gherkin
Feature: New Feature
    Scenario: Test scenario
        Given I am on the application
        When I perform an action
        Then I should see expected result
```

### 2. Implement Step Definitions
```python
@when('I perform an action')
def perform_action(driver):
    page = SomePage(driver)
    page.perform_action()
```

### 3. Create Page Objects
```python
class SomePage(BasePage):
    ELEMENT = (By.ID, "element-id")
    
    def perform_action(self):
        self.click_element(self.ELEMENT)
```

## 🧪 Test Scenarios

### Login Tests (Data-Driven)
| Username  | Password        | Expected Result   |
|-----------|-----------------|-------------------|
| demouser  | testingisfun99  | login_success     |
| demouser  | wrongpassword   | Invalid Password  |
| wronguser | testingisfun99  | Invalid Username  |

### E2E Shopping Flow
1. **Login** → Valid credentials
2. **Browse Products** → Scroll to iPhone 11 Pro
3. **Add to Cart** → Verify cart count and price
4. **Modify Quantity** → Increase to 5 items
5. **Checkout** → Fill shipping details
6. **Order Confirmation** → Verify order number
7. **Bug Testing** → Download receipt failure

### Bug Verification Tests
- **Galaxy S20 Ultra Cart Bug**: Product doesn't get added to cart
- **Download Receipt Bug**: Receipt download functionality fails

## 📊 Reporting

- **HTML Reports**: Generated in `reports/` directory
- **BrowserStack Dashboard**: Session videos and logs
- **Console Output**: Detailed test execution logs

## 🔧 Configuration

### BrowserStack Settings
```yaml
userName: anikdasgupta_sW03Uz
accessKey: gFspSApHHEnMSwGzeHk8
platforms:
  - os: Windows
    osVersion: 10
    browserName: Chrome
    browserVersion: 120.0
buildName: bstack-demo
projectName: BrowserStack Sample
debug: true
networkLogs: true
```

### pytest Configuration
```ini
[tool:pytest]
testpaths = tests
addopts = --strict-markers --html=reports/report.html -v
```

## 🐛 Known Issues & Bugs

1. **Galaxy S20 Ultra Cart Issue**
   - **Description**: Product doesn't get added to cart when clicking "Add to cart"
   - **Test**: `Scenario: End-to-end shopping with Galaxy S20 Ultra (Bug Test)`
   - **Status**: Verified and documented

2. **Download Receipt Failure**
   - **Description**: Download receipt link doesn't trigger file download
   - **Test**: `Bug verification - Download receipt failure`
   - **Status**: Verified and documented

## 🤝 Contributing

1. Add new feature files in `tests/features/`
2. Implement corresponding step definitions
3. Create page objects for new pages
4. Update this README with new test coverage
5. Ensure all tests pass before committing

## 📞 Support

For issues or questions:
- Check BrowserStack dashboard for session details
- Review HTML reports in `reports/` directory
- Verify element locators in page objects
- Check console logs for detailed error information

---

**Framework Version**: 1.0  
**Last Updated**: January 2025  
**Maintained by**: QA Team