Feature: Login functionality

  @web
  Scenario: User can log in with valid credentials
    Given I visit the login page
    When I enter next valid credentials user1 amd pass1
    Then I should see the dashboard


  @web
  Scenario: User can log in with valid credentials 2
    Given I visit the login page
    When I enter next valid credentials user2 amd pass2
    Then I should see the dashboard