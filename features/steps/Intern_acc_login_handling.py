from selenium.webdriver.common.by import By
from behave import given, when, then, step
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


EMAIL_FIELD = (By.CSS_SELECTOR, '#username')
LOGIN_BTN = (By.XPATH, "//button[@class='woocommerce-button button woocommerce-form-login__submit']")
PW_ERROR_MSG = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")
PW_FIELD = (By.CSS_SELECTOR, '#password')
USERNAME_ERROR_MSG = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")
INVALID_CREDENTIALS = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")


@given('Open Gettop acc page')
def open_gettop(context):
    context.app.gettop_pageobject.open_gettop()


@when('Click on Email field')
def email_field(context):
    context.app.gettop_pageobject.email_field()


@when('Click on PW field')
def pw_field(context):
    context.app.gettop_pageobject.pw_field()


@when('Enter email {email_input}')
def enter_email(context, email_input):
    context.app.gettop_pageobject.enter_email(email_input)


@when('Enter pw:{pw_input}')
def enter_pw(context, pw_input):
    context.app.gettop_pageobject.enter_pw(pw_input)


@then('Click on Login btn')
def click_email_btn(context):
    context.app.gettop_pageobject.click_email_btn()


@then('Verify correct pw error msg Error: {pw_required}')
def verify_pw_error_msg(context, pw_required):
    context.app.gettop_pageobject.verify_pw_error_msg(pw_required)


@then('Verify correct username error msg Error: {username_required}')
def verify_username_error_msg(context, username_required):
    # actual_result = context.driver.find_element(*USERNAME_ERROR_MSG).text
    # print(actual_result)
    # expected_result = username_required
    # assert expected_result in actual_result, f"Expected text {expected_result} did not match {actual_result}"
    context.app.gettop_pageobject.verify_username_error_msg(username_required)

@then('Verify correct credentials Error: {error_credentials}')
def verify_cred_error_msg(context, error_credentials):
    # actual_result = context.driver.find_element(*INVALID_CREDENTIALS).text
    # print(actual_result)
    # expected_result = error_credentials
    # assert expected_result in actual_result, f"Expected text {expected_result} did not match {actual_result}"
    context.app.gettop_pageobject.verify_cred_error_msg(error_credentials)
