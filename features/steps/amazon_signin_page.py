from selenium.webdriver.common.by import By
from behave import given, when, then, step
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_TXT = (By.CSS_SELECTOR, "h1")


@then('Verify Sign In page is opened')
def verify_signin_text_visible(context):
    # context.driver.wait.until(
    #     EC.url_contains('https://www.amazon.com/ap/signin'),
    #     message='Sign in page never opened'
    # )
    context.app.signin_page.verify_signin_text_visible()