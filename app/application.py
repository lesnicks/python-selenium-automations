from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
from pages.cart_page import CartPage
from pages.sign_in import SignIn

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in = SignIn(driver)

