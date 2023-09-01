from selenium.webdriver import Chrome, Safari, Firefox


# Get webdriver depending on entered --browser
def get_driver(browser_name: str):
    if browser_name == "chrome":
        return Chrome()
    elif browser_name == "safari":
        return Safari()
    elif browser_name == "firefox":
        return Firefox()
    else:
        raise AssertionError("Incorrect browser name entered. Available value: chrome, safari, firefox")

# Get url home page link depending on entered --env
def get_env_home_page_url(env: str):
    if env == "prod":
        return "https://skay.ua/uk/"
    elif env == "dev":
        return "https://dev.skay.ua/uk/"
    elif env == "stage":
        return "https://stage.skay.ua/uk/"

