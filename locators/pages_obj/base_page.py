from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

# Locators for Base page object
class BasePageLocators(BaseLocators):
    SEARCH_BAR = (By.CSS_SELECTOR, "#search_query_top")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[name=submit_search]")
    CART = (By.CSS_SELECTOR, ".title-cart")
    CART_COUNTER = (By.CSS_SELECTOR, ".ajax_cart_quantity_mod")
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, ".dropdown-toggle")
