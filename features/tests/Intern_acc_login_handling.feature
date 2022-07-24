Feature: Account Login Error Handling

  @smoke
  Scenario: User cannot login with a blank pw and sees a correct error message
    Given Open Gettop acc page
    When Click on Email field
    When Enter email test@test.com
    Then Click on Login btn
    Then Verify correct pw error msg Error: The password field is empty

    @smoke @positive
  Scenario: User cannot login with a blank email and sees a correct error message
    Given Open Gettop acc page
    When Click on PW field
    When Enter pw: test
    Then Click on Login btn
    Then Verify correct username error msg Error: Username is required.

  Scenario: User cannot login with invalid credentials and sees a correct error message
    Given Open Gettop acc page
    When Click on Email field
    When Enter email testtest.com
    When Click on PW field
    When Enter pw: a
    Then Click on Login btn
    Then Verify correct credentials Error: Unknown username. Check again or try your email address.


