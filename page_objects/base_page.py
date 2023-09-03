from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.CART.value))

    @property
    def cart_counter(self):
        element = self.wait.until(EC.element_to_be_clickable(BasePageLocators.CART_COUNTER.value))
        return element.text

    @property
    def language_button(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.LANGUAGE_BUTTON.value))


    def find_something_in_search_bar(self, something: str):
        from page_objects.products_page import ProductsPage
        self.actions.send_keys_to_element(self.search_bar, something).click(on_element=self.search_button).perform()
        return ProductsPage(webdriver=self.webdriver)

    def select_language(self, language: str):
        if language == "ua" or language == 'uk':
            button_ua = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title=Ukrainian]")))
            button_ua.click()
            from page_objects.home_page import HomePage
            sleep(3)
            assert "Популярні товари" in HomePage(webdriver=self.webdriver).popular_products_block.text, f"Failed to switch language to {language} :/"
        elif language == "ru":
            button_ru = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title=Russian]")))
            sleep(1)
            button_ru.click()
            from page_objects.home_page import HomePage
            sleep(3)
            for block in HomePage(webdriver=self.webdriver).popular_products_block:
                if "Популярные товары" in block.text:
                    assert block.is_enabled() and block.is_displayed()
        else:
            raise ValueError("Available languages: ua/uk, ru")
