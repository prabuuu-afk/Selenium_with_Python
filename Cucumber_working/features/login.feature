Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user opens the login page
    When the user enters valid username and password
    And the user clicks the Login button
    Then the user should be successfully logged in

  Scenario: Unsuccessful login with invalid credentials
    Given the user opens the login page
    When the user enters invalid username and password
    And the user clicks the Login button
    Then an error message should be displayed
  
  Scenario: Login with valid username and invalid password
    Given the user opens the login page
    When the user enters valid username and invalid password
    And the user clicks the Login button
    Then an error message should be displayed

  Scenario: Login with invalid username and valid password
    Given the user opens the login page
    When the user enters invalid username and valid password
    And the user clicks the Login button
    Then an error message should be displayed