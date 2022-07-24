# Created by bojanskaljak at 5/6/22
Feature: Test Scenarios for Amazon Support Search

  Scenario: User can search for a support option
    Given Open Amazon help page
    When Input Cancel order into search field and enter
    Then Verify Cancel Items or Orders is shown
