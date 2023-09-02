from locators.base_locators import BaseLocators
from page_objects.base_page import *
from page_objects.products_page import *


class ProductsPageLocators(BaseLocators):
    PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, " .product-container")
