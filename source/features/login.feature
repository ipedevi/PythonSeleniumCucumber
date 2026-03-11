Feature: Login functionality

  Scenario: User can log in with valid credentials
    Given I visit the login page
    When I enter next valid credentials user1 amd pass1
    Then I should see the dashboard

  Scenario: User can log in with valid credentials 2
    Given I visit the login page
    When I enter next valid credentials user2 amd pass2
    Then I should see the dashboard

  Scenario: Login fails when password is missing
    Given I visit the login page
    When I enter only username user1
    Then I should see a missing password error

  Scenario: Login fails when username is missing
    Given I visit the login page
    When I enter only password pass1
    Then I should see a missing username error
