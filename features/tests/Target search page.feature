from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

  Scenario: User can search for coffee
    Given Open target main page
    When Click on Circle tab
    Then Verify that correct search results shown for coffee

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for tea


Scenario Outline: User can search for product
  Given Open target main page
  When  Search for <search_word>
  Then Verify that correct search results shown for <search_results>
  Examples:
  |search_word | search_results |
  |coffee      | coffee         |
  |mug         | mug            |
  |tea         | tea            |
