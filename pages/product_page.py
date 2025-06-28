from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    GALAXY_S20_ULTRA = (By.XPATH, "//p[@class='shelf-item__title' and text()='Galaxy S20 Ultra']")
    IPHONE_11_PRO = (By.XPATH, "//p[@class='shelf-item__title' and text()='iPhone 11 Pro']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div.shelf-item__buy-btn")
    CART_QUANTITY = (By.CSS_SELECTOR, "span.bag__quantity")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "p.shelf-empty")
    CART_ITEM = (By.CSS_SELECTOR, "div.shelf-item")
    INCREASE_QUANTITY = (By.CSS_SELECTOR, "button.change-product-button:last-child")
    DECREASE_QUANTITY = (By.CSS_SELECTOR, "button.change-product-button:first-child")
    DELETE_ITEM = (By.CSS_SELECTOR, "div.shelf-item__del")
    SUBTOTAL = (By.CSS_SELECTOR, "p.sub-price__val")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "div.buy-btn")

    def scroll_to_product(self, product_name):
        if product_name == "Galaxy S20 Ultra":
            return self.scroll_to_element(self.GALAXY_S20_ULTRA)
        elif product_name == "iPhone 11 Pro":
            return self.scroll_to_element(self.IPHONE_11_PRO)

    def add_product_to_cart(self, product_name):
        product_element = self.scroll_to_product(product_name)
        parent_div = product_element.find_element(By.XPATH, "./ancestor::div[@class='shelf-item']")
        add_to_cart = parent_div.find_element(By.CSS_SELECTOR, "div.shelf-item__buy-btn")
        add_to_cart.click()

    def get_cart_quantity(self):
        return self.get_text(self.CART_QUANTITY)

    def get_cart_empty_message(self):
        return self.get_text(self.CART_EMPTY_MESSAGE)

    def increase_product_quantity(self):
        self.click_element(self.INCREASE_QUANTITY)

    def delete_cart_item(self):
        self.click_element(self.DELETE_ITEM)

    def get_subtotal(self):
        return self.get_text(self.SUBTOTAL)

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)