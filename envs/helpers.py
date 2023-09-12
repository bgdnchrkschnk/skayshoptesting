from selenium.webdriver import Chrome, Safari, Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options
from selenium.webdriver.firefox.options import Options


# Get webdriver depending on entered --browser
def get_driver(browser_name: str):
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        return Chrome()
    elif browser_name == "safari":
        safari_options = Options()
        safari_options.add_argument("--headless")
        return Safari(options=safari_options)
    elif browser_name == "firefox":
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        return Firefox(options=firefox_options)
    else:
        raise AssertionError("Incorrect browser name entered. Available value: chrome, safari, firefox")

# Get url home page link depending on entered --env
def get_env_home_page_url(env: str):
    if env == "prod":
        return "https://skay.ua/"
    elif env == "dev":
        return "https://dev.skay.ua/"
    elif env == "stage":
        return "https://stage.skay.ua/"

