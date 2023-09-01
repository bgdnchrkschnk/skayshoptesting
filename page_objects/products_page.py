from page_objects.base_page import *
from locators.products_page import *


class ProductsPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    @property
    def products(self):
        return self.wait.until(EC.visibility_of_all_elements_located((ProductsPageLocators.PRODUCTS_ON_PAGE.value)))
