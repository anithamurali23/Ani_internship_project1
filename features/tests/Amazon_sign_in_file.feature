Feature: Verify if logged out user can sign in when clicking on Returns and Orders


  @smoke
  Scenario: Logged out user can sign in when clicking on Returns and Orders
    Given Open amazon page
    When Click Returns and orders



  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opens


  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign in is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In disappears