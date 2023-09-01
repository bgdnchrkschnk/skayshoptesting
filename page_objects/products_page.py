from locators.pages_obj.products_page import *
from web_elements.product_item import ProductItemWebElement


class ProductsPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    @property
    def products(self):
        return self.wait.until(EC.visibility_of_all_elements_located(ProductsPageLocators.PRODUCTS_ON_PAGE.value))


    def __get_product_item_by_(self, title:str=None, article:str=None, ):
        if title:
            if len(self.products) > 1:
                for product in self.products:
                    if ProductItemWebElement(product).article == article:
                        return product
                    break
                else:
                    raise AssertionError(f"Product has not found by '{article}' article!")
        elif article:
            if len(self.products) > 1:
                for product in self.products:
                    if ProductItemWebElement(product).title == title:
                        return product
                    break
                else:
                    raise AssertionError(f"Product has not found by '{title}' title!")


    def get_product_item_by_article(self, article:str):
        product_item = self.__get_product_item_by_(article=article)
        return ProductItemWebElement(product_item)



