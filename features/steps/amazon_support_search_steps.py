from selenium.webdriver import send_keys, Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

HELP_SEARCH = (By.ID, 'helpsearch')
SEARCH_RESULT_HELP_TEXT = (By.XPATH, "//h1[text()='Cancel Items or Orders']")


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_keyword} into search field and enter')
def input_help_search(context, search_keyword):
    context.driver.find_element(*HELP_SEARCH).send_keys(search_keyword, Keys.RETURN)


@then('Verify {help_expected_result} is shown')
def verify_help_search_results(context, help_expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_HELP_TEXT).text
    assert help_expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {help_expected_result}'
    if help_expected_result == actual_result:
        print("testcase passed")
