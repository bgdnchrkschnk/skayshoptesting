import pytest
from envs.helpers import *


# Browser webdriver fixture - returns
@pytest.fixture
def webdriver(request): # request param for --browser pytest addoption value
    browser_name = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    webdriver = get_driver(browser_name=browser_name)
    webdriver.maximize_window()
    # yield HomePage(webdriver=webdriver, url)
    webdriver.quit()
