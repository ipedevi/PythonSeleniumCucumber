Feature: Api functionality

  @api
  Scenario: User can test also API
    Given I use thedogapi with my API key
    When I request a random image of a dog
    Then I should receive a valid response with the image URL
