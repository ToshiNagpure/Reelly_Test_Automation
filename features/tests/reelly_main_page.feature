Feature: Test for main page UI


  Scenario: User can go to settings and see the right number of UI elements
    Given Open the main page
    When  Log in to the page
    When Click on settings option
    Then Verify the right page opens
    Then Verify there are 11 options for the settings
    Then Verify “connect the company” button is available

