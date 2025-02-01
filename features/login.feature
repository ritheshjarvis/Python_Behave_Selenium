Feature: Verify Login Functionality

  Scenario: Verify user can Login to the site
    When user launches the website
    Then login page is displayed
    When user enters the username "standard_user"
    And user enters the password "secret_sauce"
    And user clicks on the login button
    Then home page is displayed