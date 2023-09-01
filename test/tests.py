import envs.helpers


def test_site_is_loaded(browser):
    assert browser.webdriver.current_url == envs.helpers.get_env_home_page_url(env="prod"), "Incorrect home page loaded!"
    assert browser.popular_products_block.is_displayed(), "Popular items block is absent on home page!"


def test_sales_products_all_items_with_sales_price(browser):
    browser = browser.navigate_to_sales_products()
    assert len(browser.products)>20
