import pytest
import yaml
import sys
import os
from utils.browserstack_driver import BrowserStackDriver

# Add project root to Python path for page imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def pytest_addoption(parser):
    """Add command line options for pytest"""
    parser.addoption(
        "--platform", 
        action="store", 
        default="0", 
        help="Platform index from browserstack.yml (default: 0)"
    )


@pytest.fixture(scope="session")
def browserstack_config():
    """Load BrowserStack configuration from browserstack.yml"""
    with open('browserstack.yml', 'r') as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="function")
def driver(request, browserstack_config):
    """Create WebDriver instance for each test"""
    platform_index = int(request.config.getoption("--platform"))
    platform_config = browserstack_config['platforms'][platform_index]
    
    test_name = request.node.name
    bs_driver = BrowserStackDriver()
    driver_instance = bs_driver.create_driver(platform_config, test_name)
    bs_driver.set_session_name(test_name)
    
    # Store bs_driver instance for cleanup
    request.node.bs_driver = bs_driver
    
    yield driver_instance
    
    # Mark test status based on test outcome
    if hasattr(request.node, 'rep_call'):
        if request.node.rep_call.failed:
            bs_driver.mark_test_status('failed', str(request.node.rep_call.longrepr))
        else:
            bs_driver.mark_test_status('passed')
    
    bs_driver.quit_driver()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)