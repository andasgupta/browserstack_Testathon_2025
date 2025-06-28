from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    SIGN_IN_BUTTON = (By.ID, "Sign In")
    LOGIN_BUTTON = (By.ID, "login-btn")
    USERNAME_DROPDOWN = (By.XPATH, "//div[contains(@class, 'css-1hwfws3') and .//div[contains(text(), 'Select Username')]]")
    PASSWORD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'css-1hwfws3') and .//div[contains(text(), 'Select Password')]]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3.api-error")
    LOGGED_IN_USER = (By.CSS_SELECTOR, "span.username")

    def click_sign_in(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def wait_for_login_page(self):
        self.wait_for_element_visible(self.LOGIN_BUTTON)

    def select_username(self, username):
        self.click_element(self.USERNAME_DROPDOWN)
        username_option = (By.XPATH, f"//div[contains(text(), '{username}')]")
        self.click_element(username_option)

    def select_password(self, password):
        self.click_element(self.PASSWORD_DROPDOWN)
        password_option = (By.XPATH, f"//div[contains(text(), '{password}')]")
        self.click_element(password_option)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_logged_in_username(self):
        return self.get_text(self.LOGGED_IN_USER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)