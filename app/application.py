from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage
from pages.shopping_cart_page import ShoppingCardPage
from pages.gettop_pageobject import Websitegettop
class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.shopping_cart_page = ShoppingCardPage(self.driver)
        self.gettop_pageobject = Websitegettop(self.driver)