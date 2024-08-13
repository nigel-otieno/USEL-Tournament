Feature: Tournament creation
  As a user
  I want to create a new tournament
  So that I can manage teams and matches

  Scenario: Successfully creating a new tournament
    Given I am a logged-in user
    When I go to the tournament creation page
    And I fill in the tournament details
    And I submit the form
    Then I should see a confirmation message

Feature: Team Creation
    As a logged-in user
    I want to add a new team
    So that I can score the team for the tournament

    Scenario: Successfully adding a new team
        Given I am a logged-in user
        And I have joined or created a tournament
        When I go to the tournament detail page
        And I click the create team button
        And I fill out the team create form
        And I submit the team create form
        Then I should be redirected back to my tournament
        And I will see my new team listed on the tournament