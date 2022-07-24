Feature: Tests for bestsellers functionality


  Scenario: All bestsellers links are present
    Given Open Amazon Bestsellers
    Then Verify there are 5 links


  Scenario: Verify Best Sellers links opens correct page
    Given Open Amazon page
    Given Open Amazon BestSellers
    Then Clicks on each top link and verify that correct page opens


