from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from page_objects.base_page import *


class BasePageLocators(BaseLocators):
    SEARCH_BAR = (By.CSS_SELECTOR, "#search_query_top")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[name=submit_search]")
