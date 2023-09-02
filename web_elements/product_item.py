from selenium.webdriver.remote.webelement import WebElement
from locators.web_elements.product_item import ProductItemsLocators
from page_objects.base_page import *


class ProductItemWebElement:
    def __init__(self, webelement: WebElement):
        self.__web_element = webelement

    @property
    def title(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_TITLE.by, ProductItemsLocators.PRODUCT_TITLE.locator)
        return element.text

    def old_price(self):
        pass

    @property
    def price(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_PRICE.by, ProductItemsLocators.PRODUCT_PRICE.locator)
        return element.text

    @property
    def buy_button(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_BUY_BUTTON.by, ProductItemsLocators.PRODUCT_BUY_BUTTON.locator)
        return element

    @property
    def article(self):
        element = self.__web_element.find_element(ProductItemsLocators.PRODUCT_ARTICLE.by, ProductItemsLocators.PRODUCT_TITLE.locator)
        return element.text
