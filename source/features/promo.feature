Feature: Apply promo code at checkout
  
  Background:
      Given I am on the home page
      When I book a trip to "Sant Cugat Del Valles"

  @promo
  Scenario: Apply promo code
      Given the Order Summary shows the full price "$1,243.73"
      When the user enters the promo code in the "I have a promo code" field
      And the user clicks APPLY button
      Then the price updates to the discounted price "$994.98"