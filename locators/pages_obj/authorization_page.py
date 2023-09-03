from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class AuthorizationPageLocators(BaseLocators):
    EMAIL_FIELD_REG = (By.CSS_SELECTOR, "#email_create")
    CREATE_ACCOUNT_BUTTON_REG = (By.CSS_SELECTOR, "#SubmitCreate")
    EMAIL_FIELD_SIGNIN = (By.CSS_SELECTOR, "#enail")
    CREATE_BUTTON_SIGNIN = (By.CSS_SELECTOR, "#passwd")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#SubmitLogin")
    FORGOT_PW = (By.CSS_SELECTOR, ".form-link")
    CREATE_ACCOUNT_ERROR_BLOCK = (By.CSS_SELECTOR, "#create_account_error")