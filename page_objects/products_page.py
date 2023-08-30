from page_objects.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    def __find_product_by_title(self, title: str):
        self.