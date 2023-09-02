from time import sleep
import pytest

import envs.helpers
from web_elements.product_item import ProductItemWebElement


def test_site_is_loaded(browser):
    assert browser.webdriver.current_url == envs.helpers.get_env_home_page_url(env="prod"), "Incorrect home page loaded!"
    assert browser.popular_products_block.is_displayed(), "Popular items block is absent on home page!"


def test_sales_products_all_items_with_sales_price(browser):
    browser = browser.navigate_to_sales_products()
    for product in browser.products:
        assert ProductItemWebElement(product).price, f"Sales price is absent on {ProductItemWebElement(product).title}"


def test_buy_product(browser):
    assert browser.cart_counter == "0"
    browser = browser.find_something_in_search_bar(something="00000037607-013")
    product_item = browser.get_product_item_by_article(article="00000037607-013")
    product_item.buy_button.click()
    assert browser.purchase_popup, "Purchase pop up has not been found on page!"
    sleep(2)
    assert not browser.check_product_in_popup_by_article(article="00000037607-013"), "Product has not been found by '00000037607-013' article!"
    assert not browser.cart_counter == "1"

@pytest.mark.this
def test_register_user_in_system(browser):
    browser = browser.navigate_to_authorization_page()