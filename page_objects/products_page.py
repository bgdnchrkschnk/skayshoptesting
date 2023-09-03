from locators.pages_obj.products_page import *
from page_objects.base_page import *
from web_elements.product_item import ProductItemWebElement


class ProductsPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    @property
    def products(self):
        return self.wait.until(EC.visibility_of_any_elements_located(ProductsPageLocators.PRODUCTS_ON_PAGE.value))

    @property
    def purchase_popup(self):
        return self.wait.until(EC.visibility_of_element_located(ProductsPageLocators.PURCHASE_POPUP.value))

    def __get_product_item_by_(self, title: str = None, article: str = None):
        if title:
            if len(self.products) > 1:
                for product in self.products:
                    if ProductItemWebElement(product).title == title:
                        return product
                    break
                else:
                    raise AssertionError(f"Product has not found by '{title}' title!")
        elif article:
            if len(self.products) == 1:
                return self.products[0]
            elif len(self.products) > 1:
                for product in self.products:
                    if ProductItemWebElement(product).article == article:
                        return product
                    break
                else:
                    raise AssertionError(f"Product has not found by '{article}' article!")

    def get_product_item_by_article(self, article: str):
        product_item = self.__get_product_item_by_(article=article)
        return ProductItemWebElement(webelement=product_item)


    def get_product_item_by_title(self, title: str):
        product_item = self.__get_product_item_by_(title=title)
        return ProductItemWebElement(webelement=product_item)


    def check_product_in_popup_by_article(self, article: str):
        elements = self.purchase_popup.find_elements(ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.by,
                                                     ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.locator)
        for element in elements:
            if article in element.text:
                return True
        else:
            return False


    def check_all_products_with_sale(self):
        for product in self.products:
            assert ProductItemWebElement(
                product).price, f"Sales price is absent on {ProductItemWebElement(product).title}"