from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_TXT = (By.CSS_SELECTOR, "h1")

    def verify_signin_text_visible(self):
        self.find_element(*self.SIGNIN_TXT)

