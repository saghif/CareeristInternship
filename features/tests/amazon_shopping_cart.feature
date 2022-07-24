# Created by bojanskaljak at 5/10/22
Feature: Test Scenario for default empty Shopping cart

  Scenario: Verify shopping cart is empty by default
    Given Open Amazon page
    When Clicking on Shopping Cart
    Then Verify Your Amazon Cart is empty is appearing