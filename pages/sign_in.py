from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.base_page import Page

class SignIn(Page):
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, '.sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs')


    def verify_sign_in(self):
        actual_result = self.driver.find_element(*self.VERIFY_SIGN_IN).text
        expected_result = 'Sign into your Target account'
        assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
        sleep(2)