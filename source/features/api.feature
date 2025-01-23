Feature: Api functionality

  @api
  Scenario: User can test also API
    Given I visit public marvel api
    When I obtain the first published title
    Then I can obtain deeper info from this title
