from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

#PRODUCT_NAME = (By.ID, 'productTitle')


# @when('Store product name')
# def get_product_name(context):
    # context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    # print(f'Current product: {context.product_name}')