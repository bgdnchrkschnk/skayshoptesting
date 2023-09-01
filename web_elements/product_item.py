from selenium.webdriver.remote.webelement import WebElement
from locators.web_elements.product_item import ProductItemsLocators
from page_objects.base_page import *


class ProductItemWebElement:
    def __init__(self, webelement: WebElement):
        self.__web_element = webelement

    @property
    def title(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_TITLE.value)
        return element.text

    def old_price(self):
        pass

    @property
    def price(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_PRICE.value)
        return element.text

    @property
    def buy_button(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_BUY_BUTTON.value)
        return element.text

    @property
    def article(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_ARTICLE)
        return element.text
