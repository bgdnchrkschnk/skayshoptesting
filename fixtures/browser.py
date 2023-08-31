import pytest
from envs.helpers import *
from page_objects.home_page import HomePage
from envs.helpers import *


# Browser webdriver fixture - returns
@pytest.fixture
def webdriver(request):  # request param for --browser pytest addoption value
    browser_name = request.param
    env = request.config.getoption("--env")
    url = get_env_home_page_url(env=env)
    webdriver = get_driver(browser_name=browser_name)
    webdriver.maximize_window()
    yield HomePage(webdriver=webdriver, url=url)
    webdriver.quit()
