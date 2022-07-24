from selenium.webdriver.common.by import By
from pages.page_base_gettop import Gettop
from selenium.webdriver.common.action_chains import ActionChains


class Websitegettop(Gettop):
    EMAIL_FIELD = (By.CSS_SELECTOR, '#username')
    LOGIN_BTN = (By.XPATH, "//button[@class='woocommerce-button button woocommerce-form-login__submit']")
    PW_ERROR_MSG = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")
    PW_FIELD = (By.CSS_SELECTOR, '#password')
    USERNAME_ERROR_MSG = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")
    INVALID_CREDENTIALS = (By.XPATH, "//div[@class='message-container container alert-color medium-text-center']")

    def open_gettop(self):
        self.open_page('https://gettop.us/my-account/')

    def email_field(self):
        self.driver.find_element(*self.EMAIL_FIELD).click()

    def pw_field(self):
        self.driver.find_element(*self.PW_FIELD).click()

    def enter_email(self, email_input):
        self.input_text(email_input, *self.EMAIL_FIELD)

    def enter_pw(self, pw_input):
        self.input_text(pw_input, *self.PW_FIELD)

    def click_email_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def verify_pw_error_msg(self, pw_required):
        actual_result = self.driver.find_element(*self.USERNAME_ERROR_MSG).text
        print(actual_result)
        assert pw_required in actual_result, \
            f' Expected {pw_required} does not match actual {actual_result}'

    def verify_username_error_msg(self, username_required):
        actual_result = self.driver.find_element(*self.USERNAME_ERROR_MSG).text
        print(actual_result)
        assert username_required in actual_result, \
            f' Expected {username_required} does not match actual {actual_result}'

    def verify_cred_error_msg(self, error_credentials):
        actual_result = self.driver.find_element(*self.USERNAME_ERROR_MSG).text
        print(actual_result)
        assert error_credentials in actual_result, \
            f' Expected {error_credentials} does not match actual {actual_result}'

