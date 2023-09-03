from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class AuthorizationPageRegistrationLocators(BaseLocators):
    EMAIL_FIELD_REG = (By.CSS_SELECTOR, "#email_create")
    CREATE_ACCOUNT_BUTTON_REG = (By.CSS_SELECTOR, "#SubmitCreate")
    CREATE_ACCOUNT_ERROR_BLOCK = (By.CSS_SELECTOR, "#create_account_error")

class AuthorizationPageSignInLocators(BaseLocators):
    EMAIL_FIELD_SIGNIN = (By.CSS_SELECTOR, "#email")
    CREATE_BUTTON_SIGNIN = (By.CSS_SELECTOR, "#passwd")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#SubmitLogin")

class AuthorizationPageForgotPwLocators(BaseLocators):
    FORGOT_PW = (By.CSS_SELECTOR, ".form-link")
    EMAIL_FIELD_FORGOT_PW = (By.CSS_SELECTOR, "#email")
    CONFIRM_EMAIL_FORGOT_PW_BUTTON = (By.CSS_SELECTOR, "[type=submit].button-medium")
    ALERT_SUCCESS_BLOCK = (By.CSS_SELECTOR, ".alert-success")
