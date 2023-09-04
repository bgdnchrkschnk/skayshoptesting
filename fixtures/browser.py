import allure
import pytest

import envs.helpers
from envs.helpers import *
from page_objects.home_page import HomePage
from envs.helpers import *


# Browser webdriver fixture - returns initialized webdriver
@pytest.fixture
@allure.title(f"Navigate to home page {envs.helpers.get_env_home_page_url(env='prod')}")
def browser(request):  # request param for --browser pytest addoption value
    browser_name = request.param
    env = request.config.getoption("--env")
    url = get_env_home_page_url(env=env)
    driver = get_driver(browser_name=browser_name)
    driver.maximize_window()
    yield HomePage(webdriver=driver, url=url)
    driver.quit()
