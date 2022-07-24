from selenium.webdriver.common.by import By
from pages.base_page import Page


class ShoppingCardPage(Page):
    SHOPPING_CART = (By.ID, 'nav-cart')
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def clicking_cart_btn(self):
        self.find_element(*self.SHOPPING_CART).click()

    def shopping_cart_empty(self, cart_expected_result):
        actual_result = self.driver.find_element(*self.EMPTY_CART).text
        assert cart_expected_result == actual_result, \
            f' Expected {cart_expected_result} does not match actual {actual_result}'
