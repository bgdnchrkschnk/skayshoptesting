from allure import step
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.pages_obj.base_page import *


# Implement class of general mutual elements of all pages to interact with
class BasePage:

    # Initialize webdriver, WebDriverWait and ActionChains objects for pages
    def __init__(self, webdriver, logger):
        self.__webdriver = webdriver
        self.__wait = WebDriverWait(self.webdriver, 15)
        self.__actions = ActionChains(self.webdriver)
        self.__logger = logger

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

    @property
    def logger(self):
        return self.__logger

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

    @step("Find product in search bar")
    def find_something_in_search_bar(self, something: str):
        try:
            self.logger.debug(f"Sending keys {something} to search bar element.. Then clicking on search button")
            self.logger.debug(f"Clicking on search button")
            from page_objects.products_page import ProductsPage
            self.actions.send_keys_to_element(self.search_bar, something).click(on_element=self.search_button).perform()
            return ProductsPage(webdriver=self.webdriver, logger=self.logger)
        except TimeoutError as te:
            self.logger.error(f"Unsuccessful sending keys - {something} into search bar element and clicking on search button")
            raise TimeoutError(str(te))


    @step("Switch site language")
    def select_language(self, language: str):
        try:
            if language == "ua" or language == 'uk':
                self.logger.debug(f"Searching for {language} button on UI")
                button_ua = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title=Ukrainian]")))
                self.logger.debug("Clicking on it..")
                button_ua.click()
                self.logger.debug(f"Asserting that 'Товари зі знижками' is visible on main page..")
                assert self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "//a[contains(text(), 'Товари зі знижками')]")))
            elif language == "ru":
                self.logger.debug(f"Searching for {language} button on UI")
                button_ru = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title=Russian]")))
                self.logger.debug("Clicking on it..")
                button_ru.click()
                self.logger.debug(f"Asserting that 'Товары со скидками' is visible on main page..")
                assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Товары со скидками')]")))
            else:
                raise ValueError("Available languages: ua/uk, ru")
        except TimeoutError as te:
            self.logger.error(f"{language} button has not been found on page!")
            raise TimeoutError(str(te))
