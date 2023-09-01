from enum import Enum

from web_elements.product_item import *


class ProductItemsLocators(Enum):
    PRODUCT_TITLE = (By.CSS_SELECTOR, " .product-name>span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, " .new-item-price.product-price")
    PRODUCT_ARTICLE = (By.CSS_SELECTOR, " .item-refeence-id:last-child")
    PRODUCT_BUY_BUTTON = (By. CSS_SELECTOR, " .product-container a.ajax_add_to_cart_button")