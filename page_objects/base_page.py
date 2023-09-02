from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.pages_obj.base_page import *




# Implement class of general mutual elements of all pages to interact with
class BasePage:

    # Initialize webdriver, WebDriverWait and ActionChains objects for pages
    def __init__(self, webdriver):
        self.__webdriver = webdriver
        self.__wait = WebDriverWait(self.webdriver, 15)
        self.__actions = ActionChains(self.webdriver)

    # Set driver objects as properties
    @property
    def webdriver(self):
        return self.__webdriver

    @property
    def wait(self):
        return self.__wait

    @property
    def actions(self):
        return self.__actions

    # General base elements to interact with
    @property
    def search_bar(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.SEARCH_BAR.value))

    @property
    def search_button(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.SEARCH_BUTTON.value))

    @property
    def cart(self):
        return self.wait.until(EC.element_to_be_clickable((BasePageLocators.CART.value)))


    def find_something_in_search_bar(self, something: str):
        from page_objects.products_page import ProductsPage
        self.actions.send_keys_to_element(self.search_bar, something).click(on_element=self.search_button).perform()
        return ProductsPage(webdriver=self.webdriver)


