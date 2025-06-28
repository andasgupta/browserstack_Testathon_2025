import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class BrowserStackDriver:
    def __init__(self):
        self.driver = None
        self.username = os.getenv('BROWSERSTACK_USERNAME', 'anikdasgupta_sW03Uz')
        self.access_key = os.getenv('BROWSERSTACK_ACCESS_KEY', 'gFspSApHHEnMSwGzeHk8')
        self.hub_url = f"https://{self.username}:{self.access_key}@hub-cloud.browserstack.com/wd/hub"

    def create_driver(self, platform_config, test_name=None):
        """Create WebDriver instance for BrowserStack"""
        capabilities = {
            'browserstack.user': self.username,
            'browserstack.key': self.access_key,
            'project': 'BrowserStack Sample',
            'build': 'bstack-demo',
            'browserstack.debug': True,
            'browserstack.networkLogs': True,
            'browserstack.console': 'info'
        }
        
        # Add platform-specific capabilities
        capabilities.update(platform_config)
        
        if test_name:
            capabilities['name'] = test_name

        # Create appropriate options based on browser
        browser_name = platform_config.get('browserName', '').lower()
        if 'chrome' in browser_name:
            options = ChromeOptions()
        elif 'firefox' in browser_name:
            options = FirefoxOptions()
        elif 'safari' in browser_name:
            options = SafariOptions()
        else:
            options = ChromeOptions()  # Default to Chrome

        self.driver = webdriver.Remote(
            command_executor=self.hub_url,
            options=options,
            desired_capabilities=capabilities
        )
        
        return self.driver

    def set_session_name(self, name):
        """Set session name for BrowserStack reporting"""
        if self.driver:
            executor_object = {
                'action': 'setSessionName',
                'arguments': {'name': name}
            }
            browserstack_executor = f'browserstack_executor: {json.dumps(executor_object)}'
            self.driver.execute_script(browserstack_executor)

    def mark_test_status(self, status, reason=""):
        """Mark test as passed or failed"""
        if self.driver:
            executor_object = {
                'action': 'setSessionStatus',
                'arguments': {
                    'status': status,
                    'reason': reason
                }
            }
            browserstack_executor = f'browserstack_executor: {json.dumps(executor_object)}'
            self.driver.execute_script(browserstack_executor)

    def quit_driver(self):
        """Quit the WebDriver instance"""
        if self.driver:
            self.driver.quit()
            self.driver = None