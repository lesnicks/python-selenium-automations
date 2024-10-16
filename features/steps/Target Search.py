from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(2)

@when('Search for {item}')
def search_product(context, item):
    # print(item)
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys(item)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(8)  # Wait for page to load

@then('Verify that correct search results shown for {product}')
def verify_cart_empty(context, product):
    context.app.search_results_page.verify_results(product)