from locators.pages_obj.products_page import *
from page_objects.base_page import *
from web_elements.product_item import ProductItemWebElement
from allure import step


class ProductsPage(BasePage):
    def __init__(self, webdriver, logger):
        super().__init__(webdriver=webdriver, logger=logger)

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
        try:
            self.logger.debug(f"Searching product item by article {article}")
            product_item = self.__get_product_item_by_(article=article)
            return ProductItemWebElement(webelement=product_item)
        except:
            self.logger.error(f"The product item with article {article} is not found!")

    def get_product_item_by_title(self, title: str):
        try:
            self.logger.debug(f"Searching product item by title {title}")
            product_item = self.__get_product_item_by_(title=title)
            return ProductItemWebElement(webelement=product_item)
        except:
            self.logger.error(f"The product item with title {title} is not found!")

    @step("Check that product is present in cart pop up")
    def check_product_in_cart_popup_by_article(self, article: str):
        self.logger.debug(f"Collecting all found product items by {ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.by,ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.locator} locator...")
        elements = self.purchase_popup.find_elements(ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.by,
                                                     ProductsPageLocators.PURCHASE_POPUP_ARTICLE_DIV.locator)
        self.logger.debug(f"Checking each product item to contain {article} article in cart pop up..")
        for element in elements:
            if article in element.text:
                return True
        else:
            return False

    @step("Check that each product on page has sale price")
    def check_all_products_with_sale(self):
        self.logger.debug("Initializating each product item in ProductItemWebElement to check if .price property present (sale price)")
        for product in self.products:
            assert ProductItemWebElement(
                product).price, f"Sales price is absent on {ProductItemWebElement(product).title}"
