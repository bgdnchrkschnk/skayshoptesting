from locators.pages_obj.home_page import *
from page_objects.base_page import *
from allure import step


# Implement class home page elements to interact with
class HomePage(BasePage):
    def __init__(self, webdriver, url):
        super().__init__(webdriver=webdriver)
        self.webdriver.get(url=url)

    # Set as property to return popular product block
    @property
    def popular_products_block(self):
        return self.wait.until(EC.visibility_of_any_elements_located(HomePageLocators.POPULAR_BLOCK.value))

    @step("Navigate to sale products page")
    def navigate_to_sales_products(self):
        from page_objects.products_page import ProductsPage
        self.webdriver.get("https://skay.ua/uk/prices-drop/")
        return ProductsPage(webdriver=self.webdriver)

    @step("Navigate to Authorization page")
    def navigate_to_authorization_page(self):
        from page_objects.authorization_page import AuthorizationPage
        self.webdriver.get("https://skay.ua/uk/authentication/")
        return AuthorizationPage(webdriver=self.webdriver)

    @step("Check that popular products block is displayed on page")
    def check_popular_products_block_is_displayed(self):
        state = False
        while not state:
            for block in self.popular_products_block:
                if block.is_displayed() and block.is_enabled():
                    state = True
                    break
            return True if state else False


