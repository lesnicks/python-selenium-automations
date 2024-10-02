Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Click on Cart icon
    Then Verify Cart is empty

  Scenario: User can see product in cart
    Given Open the target.com
    When Search for coffee
    Then Click on Add to Cart button
    Then Verify adding to cart
    Then Verify cart has 1 item(s)

