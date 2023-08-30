from page_objects.base_page import BasePage


# Implement class home page elements to interact with
class HomePage(BasePage):
    def __init__(self, webdriver, url):
        super().__init__(webdriver=webdriver)
        self.webdriver.get(url=url)