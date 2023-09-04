
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

# Locators for Home page object
class HomePageLocators(BaseLocators):
    POPULAR_BLOCK = (By.CSS_SELECTOR, " .h4.page-subheading")
