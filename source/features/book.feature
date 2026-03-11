Feature: Book a space trip

  Scenario: Successfully book a trip to Sant Cugat Del Valles
    Given I am on the home page
    When I book a trip to Sant Cugat Del Valles
    Then I should see the trip price

  Scenario: Valencia is not available as a destination
    Given I am on the home page
    Then Valencia should not be available as a destination
