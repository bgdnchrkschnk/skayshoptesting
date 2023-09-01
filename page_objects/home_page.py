from page_objects.base_page import *
from locators.home_page import *


# Implement class home page elements to interact with
class HomePage(BasePage):
    def __init__(self, webdriver, url):
        super().__init__(webdriver=webdriver)
        self.webdriver.get(url=url)

    # Set as property to return popular product block
    @property
    def popular_products_block(self):
        return self.wait.until(EC.visibility_of_any_elements_located(HomePageLocators.POPULAR_BLOCK.value))[1]

    def navigate_to_sales_products(self):
        from page_objects.products_page import ProductsPage
        self.webdriver.get("https://skay.ua/uk/prices-drop/")
        return ProductsPage(webdriver=self.webdriver)
