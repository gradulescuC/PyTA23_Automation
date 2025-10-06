Feature: This feature will validate the functionality of the login page

#Scenario: Validate that when user inserts proper username and password and presses login button, login is successful
 Scenario: Positive Testing: Valid username, valid password =≥ Login successful
   Given I am on the saucedemo homepage
   When I insert username
   And I insert password
   And I click the login button
   Then I should be logged in and I should see the saucedemo inventory homepage