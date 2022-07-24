Feature: Tests for Amazon search

  @smoke
  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word  |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |


  Scenario: Product gets added to the cart
    Given Open Amazon page
    When Search for lol surprise omg doll
    And Click on the first product
    And Click on Add to cart btn
    Then Verify cart has 1 item


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    Then Verify hamburger menu btn present


  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links


  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present


  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by <dept_alias>
    And Search for <search_query>
    Then Verify <selected_dept> department is selected
    Examples:
    |dept_alias   |search_query   |selected_dept   |
    |stripbooks   |faust   |books   |
    |audible   |Alice in   |audible   |