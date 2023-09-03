from time import sleep
import pytest

import envs.helpers
from web_elements.product_item import ProductItemWebElement


def test_site_is_loaded(browser):
    assert browser.webdriver.current_url == "https://skay.ua/uk/", "Incorrect home page loaded!"
    assert browser.check_popular_products_block_is_displayed(), "Popular items block is absent on home page!"


def test_sales_products_all_items_with_sales_price(browser):
    browser = browser.navigate_to_sales_products()
    browser.check_all_products_with_sale()


def test_buy_product(browser):
    assert browser.cart_counter == "0"
    browser = browser.find_something_in_search_bar(something="00000037607-013")
    product_item = browser.get_product_item_by_article(article="00000037607-013")
    product_item.buy_button.click()
    assert browser.purchase_popup, "Purchase pop up has not been found on page!"
    assert browser.check_product_in_popup_by_article(article="00000037607-013"), "Product has not been found by '00000037607-013' article!"
    assert browser.cart_counter == "1"

# @pytest.mark.this
def test_site_language(browser):
    assert browser.language_button, "Language button is not found on page!"
    browser.language_button.click()
    browser.select_language(language="ru")


def test_register_already_used_email(browser):
    browser = browser.navigate_to_authorization_page()
    browser.signup(email="bgdnchrkschnk@gmail.com")
    assert browser.create_account_error_block, "Error block has not asserted on page after existing email entered to signup"