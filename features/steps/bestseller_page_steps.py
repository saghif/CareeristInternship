from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.app.bestsellers_page.open_bestsellers()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    # actual_links = context.driver.find_elements(*TOP_LINKS)
    # assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'
    context.app.bestsellers_page.verify_links_preset(expected_links)




