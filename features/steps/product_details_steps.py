from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name .imgSwatch")
COLOR_NAME = (By.CSS_SELECTOR, "span.selection")
SHIRT_COLORS = (By.CSS_SELECTOR, "#variation_color_name li[class*='swatch']")
SHIRT_COLOR_NAME = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.invisibility_of_element_located(ADD_TO_CART_BTN))


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('User hovers over New Arrivals')
def hover_over_options(context):
    context.app.header.hover_over_options()


@then('Verifies user sees the deals')
def verify_fashion_deals(context):
    context.app.header.verify_fashion_deals()


@then('Verify user can click through colors')
def verify_clicking_colors(context):
    expected_colors = ['Black', 'Solid Black', 'Navy']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        option.click()
        sleep(2)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'


@then('Verify correct color has been selected')
def verify_correct_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown']
    actual_colors = []

    shirt_colors = context.driver.find_elements(*SHIRT_COLORS)
    for color in shirt_colors[:4]:
        color.click()
        sleep(1)
        shirt_color_name = context.driver.find_element(*SHIRT_COLOR_NAME).text
        actual_colors += [shirt_color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'
