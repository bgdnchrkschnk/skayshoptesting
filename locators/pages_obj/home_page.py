from enum import Enum

from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators
from page_objects.home_page import *


class HomePageLocators(BaseLocators):
    POPULAR_BLOCK = (By.CSS_SELECTOR, " .h4.page-subheading")
