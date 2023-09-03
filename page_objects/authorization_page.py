from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import *
from locators.pages_obj.authorization_page import AuthorizationPageRegistrationLocators, AuthorizationPageSignInLocators, AuthorizationPageForgotPwLocators


class AuthorizationPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    """
    REGISTRATION BLOCK--------------------------------------------------------------------------------------------------
    """

    @property
    def email_field_reg(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageRegistrationLocators.EMAIL_FIELD_REG.value))

    @property
    def create_account_button_reg(self):
        return self.wait.until(
            EC.element_to_be_clickable(AuthorizationPageRegistrationLocators.CREATE_ACCOUNT_BUTTON_REG.value))

    def signup(self, email: str):
        self.actions \
            .send_keys_to_element(self.email_field_reg, email) \
            .pause(2) \
            .click(self.create_account_button_reg) \
            .pause(1) \
            .perform()

    @property
    def create_account_error_block(self):
        return self.wait.until(
            EC.presence_of_element_located(AuthorizationPageRegistrationLocators.CREATE_ACCOUNT_ERROR_BLOCK.value))

    """
    SIGN IN BLOCK ------------------------------------------------------------------------------------------------------
    """

    @property
    def email_field_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.EMAIL_FIELD_SIGNIN.value))

    @property
    def create_account_button_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.CREATE_BUTTON_SIGNIN.value))

    @property
    def sign_in_button(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.SIGN_IN_BUTTON.value))

    @property
    def forgot_pw(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.FORGOT_PW.value))

    """
    FORGOT PW BLOCK--------------------------------------------------------------------------------------------------
    """

    @property
    def email_forgot_pw(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.EMAIL_FIELD_FORGOT_PW.value))

    @property
    def confirm_email_forgot_pw_button(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.CONFIRM_EMAIL_FORGOT_PW_BUTTON.value))

    # Success message block after email entered in forgot pw
    @property
    def alert_success_block(self):
        return self.wait.until(EC.presence_of_element_located(AuthorizationPageForgotPwLocators.ALERT_SUCCESS_BLOCK.value))

    def enter_email_forgot_pw(self, email: str):
        self.actions.send_keys_to_element(self.email_forgot_pw, email).pause(1).click(self.confirm_email_forgot_pw_button).pause(2).perform()
