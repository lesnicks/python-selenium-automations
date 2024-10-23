from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open the Target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(4)

@when('Click on sign in')
def sign_in(context):
    context.app.main_page.sign_in()
    sleep(5)  # wait for search results page to load


@then('From right side navigation menu, click Sign In')
def verify_results(context):
    context.app.header.verify_results()
    sleep(5)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in.verify_sign_in()


