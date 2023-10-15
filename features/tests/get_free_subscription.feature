# Created by anithamurali at 10/14/23
Feature: verify the get free subscription opens in the new tab

  Scenario: verify the get free subscription opens in the new tab
    Given Open the main page
    When Log in to the page
    Then Click on Get a free subscription
    Then Switch the new tab
    And  Verify the Get a month of free subscription! in the new tab