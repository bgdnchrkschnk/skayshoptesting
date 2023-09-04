from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


# Locators for Products page object
class ProductsPageLocators(BaseLocators):
    PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, " .product-container")
    PURCHASE_POPUP = (By.CSS_SELECTOR, ".layer_cart_product")
    PURCHASE_POPUP_ARTICLE_DIV = (By.CSS_SELECTOR, ".cart-reference")
