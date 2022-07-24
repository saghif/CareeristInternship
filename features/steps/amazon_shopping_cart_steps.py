from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then

SHOPPING_CART = (By.ID, 'nav-cart')
EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@when('Clicking on Shopping Cart')
def clicking_cart_btn(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SHOPPING_CART))
    # context.driver.find_element(*SHOPPING_CART).click()
    context.app.shopping_cart_page.clicking_cart_btn()


@then('Verify {cart_expected_result} is appearing')
def shopping_cart_empty(context, cart_expected_result):
    #actual_result = context.driver.find_element(*EMPTY_CART_TEXT).text
    # assert cart_expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {cart_expected_result}'
    # if cart_expected_result == actual_result:
    #     print("testcase passed")
    context.app.shopping_cart_page.shopping_cart_empty(cart_expected_result)
