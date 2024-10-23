from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    NAV_SIGN_IN = (By.CSS_SELECTOR, '.sc-859e7637-0.hHZPQy')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(2)


    def verify_results(self):
        self.click(*self.NAV_SIGN_IN)
        sleep(2)


