from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the Target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(4)

@when('Click on sign in')
def search_product(context):
    #Click cart
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-58ad44c0-3 kwbrXj h-margin-r-x3').click()
    sleep(5)  # wait for search results page to load


@then('From right side navigation menu, click Sign In')
def verify_results(context):
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-859e7637-0 hHZPQy').click()
    sleep(5)

@then('Verify Sign In form opened')
def verify_results(context):
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-58ad44c0-3 kwbrXj h-margin-r-x3').click()
    actual_result = context.driver.find_element(By.CSS_SELECTOR, value='.sc-859e7637-0 hHZPQy').click()
    expected_result = ''
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    print('test case is passed')


