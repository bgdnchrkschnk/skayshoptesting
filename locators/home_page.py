from enum import Enum

from page_objects.home_page import *


class HomePageLocators(Enum):
    POPULAR_BLOCK = (By.CSS_SELECTOR, ".h4.page-subheading")
