from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from selenium import webdriver

PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
PRIVACY_PAGE = (By.CSS_SELECTOR, "div.cs-help-content")


@given('Open Amazon T&C page')
def amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("/nAfter clicking, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def notice_page_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window and switch back to original')
def close_window_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


