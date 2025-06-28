from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators
    ORDER_SUMMARY_TITLE = (By.CSS_SELECTOR, "h3.cart-title")
    ITEM_COUNT = (By.CSS_SELECTOR, "h3.cart-section-heading")
    TOTAL_PRICE = (By.CSS_SELECTOR, "span.cart-priceItem-value span")
    FIRST_NAME = (By.ID, "firstNameInput")
    LAST_NAME = (By.ID, "lastNameInput")
    ADDRESS = (By.ID, "addressLine1Input")
    STATE = (By.ID, "provinceInput")
    POSTAL_CODE = (By.ID, "postCodeInput")
    SUBMIT_BUTTON = (By.ID, "checkout-shipping-continue")
    CONFIRMATION_MESSAGE = (By.ID, "confirmation-message")
    ORDER_NUMBER = (By.XPATH, "//strong")
    DOWNLOAD_RECEIPT = (By.ID, "downloadpdf")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "button.button--tertiary")

    def get_order_summary_title(self):
        return self.get_text(self.ORDER_SUMMARY_TITLE)

    def get_item_count(self):
        return self.get_text(self.ITEM_COUNT)

    def get_total_price(self):
        return self.get_text(self.TOTAL_PRICE)

    def fill_shipping_form(self, first_name, last_name, address, state, postal_code):
        self.find_element(self.FIRST_NAME).send_keys(first_name)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.ADDRESS).send_keys(address)
        self.find_element(self.STATE).send_keys(state)
        self.find_element(self.POSTAL_CODE).send_keys(postal_code)

    def submit_order(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_order_number(self):
        return self.get_text(self.ORDER_NUMBER)

    def click_download_receipt(self):
        self.click_element(self.DOWNLOAD_RECEIPT)

    def click_continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING)