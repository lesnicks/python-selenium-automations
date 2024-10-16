from pages.header import Header
from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results_page import SeachResultsPage

class application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SeachResultsPage(driver)
