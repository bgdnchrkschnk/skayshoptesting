from enum import Enum
from page_objects.products_page import *


class ProductsPageLocators(Enum):
    PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, ".product-container")
