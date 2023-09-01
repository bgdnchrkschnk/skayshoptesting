from enum import Enum
from selenium.webdriver.common.by import By

class CssBasePageLocators(Enum):
    SEARCH_BAR = (By.CSS_SELECTOR, "#search_query_top")

class XpathBasePageLocators(Enum):
    SEARCH_BAR = (By.XPATH, "//*[@id='search_query_top']")