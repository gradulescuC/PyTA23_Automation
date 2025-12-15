@all
Feature: This feature will validate the functionality of the login page

  Background:
     Given I am on the saucedemo homepage
#Scenario: Validate that when user inserts proper username and password and presses login button, login is successful
 @regression @login
  Scenario: Positive Testing: Valid username, valid password =≥ Login successful
   When I insert username
   And I insert password
   And I click the login button
   Then I should be logged in and I should see the saucedemo inventory homepage

@sanity @regression @login @negative
Scenario Outline: Negative Testing: Login unsuccessful - INVALID CREDENTIALS
   When I insert username "<username_value>"
   And I insert password "<password_value>"
   And I click the login button
   Then I should receive an unsuccessful login message: "<expected_error_message>"
  Examples:
    | username_value | password_value | expected_error_message                                                    |
    | standard_user  | secret_sauce1  | Epic sadface: Username and password do not match any user in this service |
    | standard_user1 | secret_sauce   | Epic sadface: Username and password do not match any user in this service |
    | standard_user1 | secret_sauce1  | Epic sadface: Username and password do not match any user in this service |
    | standard_user  | null           | Epic sadface: Password is required                                        |
    | standard_user1 | null           | Epic sadface: Password is required                                        |
    | null           | secret_sauce   | Epic sadface: Username is required                                        |
    | null           | secret_sauce1  | Epic sadface: Username is required                                        |
    | null           | null           | Epic sadface: Username is required                                        |

# scenario outline
# rulare cu raport de executie
# rulare cu tag-uri
# rularea a unui singur feature file folosind terminalul
# background