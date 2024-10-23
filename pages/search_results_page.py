from selenium.webdriver.common.by import By

from pages.base_page import Page

from time import sleep


class SearchResultPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")



    def verify_results(self, product):
        actual_result = self.driver.find_elements(*self.SEARCH_RESULTS_HEADER).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        sleep(2)
        self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
        sleep(5)

    def store_product_name(self):
        self.wait_for_element_to_appear(*self.SIDE_NAV_PRODUCT_NAME)
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Product name: {product_name}')

    def click_add_to_cart_side_bar(self):
        self.click(*self.ADD_TO_CART_BTN_SIDE_NAV)
        sleep(2)


