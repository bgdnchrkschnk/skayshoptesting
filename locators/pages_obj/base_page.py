from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from page_objects.base_page import *

class CssBasePageLocators(BaseLocators):
    SEARCH_BAR = (By.CSS_SELECTOR, "#search_query_top")

class XpathBasePageLocators(BaseLocators):
    SEARCH_BAR = (By.XPATH, "//*[@id='search_query_top']")