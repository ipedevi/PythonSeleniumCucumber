Feature: Book a space trip

  @book
  Scenario: Successfully book a trip to Destination
    Given I am on the home page
    When I book a trip to "Sant Cugat Del Valles"
    Then I should see the trip price

  @checkout
  Scenario: Complete checkout for Destination
    Given I am on the home page
    When I book a trip to "Sant Cugat Del Valles"
    When the user enters "John Doe" in the Name field
    And the user enters "john@test.com" in the Email Address field
    And the user enters "123-45-6789" in the Social Security Number field
    And the user enters "555-1234" in the Phone Number field
    Then the button on the "Sant Cugat Del Valles" card displays "BOOKED"