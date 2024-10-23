from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def open_main(self):
        self.open('https://www.target.com/')

    def click_cart(self):
        self.click(*self.CART_BTN)

