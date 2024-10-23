from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text}, did not match {actual_text}'

    def open_cart(self):
        self.open('https://www.target.com/cart')
        sleep(3)

    def verify_cart_items(self, amount):
        self.wait_for_element_to_appear(*self.CART_SUMMARY)
        cart_items = self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_items, f"Expected {amount} items but got {cart_items}"
        print(f'Cart item: {cart_items}')

    def verify_product_name(self):
        product_name = self. find_element(*self.CART_ITEM_TITLE)
        print(f'actual product in cart name: {product_name}')