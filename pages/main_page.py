from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.CSS_SELECTOR, '.sc-58ad44c0-3.kwbrXj.h-margin-r-x3')

    def open_main(self):
        self.open('https://www.target.com/')

    def click_cart(self):
        self.click(*self.CART_BTN)

    def sign_in(self):
        self.click(*self.SIGN_IN)

