from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, webdriver):

        # Initialize webdriver, WebDriverWait and ActionChains objects for pages
        self.__webdriver = webdriver
        self.__wait = WebDriverWait(self.webdriver, 15)
        self.__actions = ActionChains


    # Set driver objects as properties

    @property
    def webdriver(self):
        return self.__webdriver

    @property
    def wait(self):
        return self.__wait

    @property
    def actions(self):
        return self.__actions

