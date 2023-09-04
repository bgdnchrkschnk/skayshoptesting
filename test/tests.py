import os
from time import sleep
import pytest
from allure import attach, attachment_type, title, description, severity, severity_level
import envs.helpers
from web_elements.product_item import ProductItemWebElement

@pytest.mark.this
@title("Check site is correctly loaded")
@description("Test verifies if site was correctly loaded")
@severity(severity_level.CRITICAL)
def test_site_is_loaded(browser):
    assert browser.webdriver.current_url == "https://skay.ua/uk/", "Incorrect home page loaded!"
    assert browser.check_popular_products_block_is_displayed(), "Popular items block is absent on home page!"


@title("Check all items are with sales price on sales products page")
@description("Test checks that each item on sales products page has sale price")
def test_sales_products_all_items_with_sales_price(browser):
    browser = browser.navigate_to_sales_products()
    browser.check_all_products_with_sale()


@title("Check buy product")
@description("Check product is in cart after click on buy button (screenshot attached)")
def test_buy_product(browser):
    assert browser.cart_counter == "0"
    browser = browser.find_something_in_search_bar(something="00000037607-013")
    product_item = browser.get_product_item_by_article(article="00000037607-013")
    product_item.buy_button.click()
    assert browser.purchase_popup, "Purchase pop up has not been found on page!"
    assert browser.check_product_in_cart_popup_by_article(article="00000037607-013"), "Product has not been found by '00000037607-013' article!"
    assert browser.cart_counter == "1"
    attach(browser.webdriver.get_screenshot_as_png(), name="Item in cart - proof!")


@title("Check switching site language")
@description("Test switches site language to russian and make a sure of it")
def test_site_language(browser):
    assert browser.language_button, "Language button is not found on page!"
    browser.language_button.click()
    browser.select_language(language="ru")


@title("Check system does not allow to register previously registered email in system")
@description("Test fills out previously registered in system email and verifies its not accepted")
def test_register_already_used_email(browser):
    browser = browser.navigate_to_authorization_page()
    browser.signup(email="bgdnchrkschnk@gmail.com")
    browser.create_account_button_reg.click()
    assert browser.create_account_error_block, "Error block has not asserted on page after existing email entered to signup"
    attach(browser.webdriver.get_screenshot_as_png(), name="Pay attention to error block")


@title("Check system successfully accepted email in forgot pw")
@description("Test provides email in email field of forgot pw module and checks if success pop up was displayed on page")
def test_forgot_pw_is_correct(browser):
    browser = browser.navigate_to_authorization_page()
    browser.forgot_pw.click()
    sleep(3)
    browser.enter_email_forgot_pw(email="bgdnchrkschnk@gmail.com")
    browser.confirm_email_forgot_pw_button.click()
    assert browser.alert_success_block.is_displayed(), "No success message block after email was sent in forgot pw!"