import allure
import pytest
from page_objects.home_page import HomePage
from envs.helpers import *


# Browser webdriver fixture - returns initialized webdriver
@pytest.fixture
@allure.title(f"Navigate to home page {get_env_home_page_url(env='prod')}")
def browser(request, custom_logger):  # request param for --browser pytest addoption value
    browser_name = request.param
    env = request.config.getoption("--env")
    url = get_env_home_page_url(env=env)
    driver = get_driver(browser_name=browser_name)
    driver.maximize_window()
    custom_logger.info(f"Webdriver {browser_name} initialized successfully")
    custom_logger.info(f"Webdriver is going to connect for {env}..")
    custom_logger.info(f"Connecting to {url}..")
    yield HomePage(webdriver=driver, logger=custom_logger, url=url)
    custom_logger.info(f"Quiting webdriver {browser_name}... Session closed")
    driver.quit()
