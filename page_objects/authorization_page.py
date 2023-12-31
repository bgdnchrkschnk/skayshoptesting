from selenium.webdriver.remote.webelement import WebElement
from allure import step
from page_objects.base_page import *
from locators.pages_obj.authorization_page import AuthorizationPageRegistrationLocators, \
    AuthorizationPageSignInLocators, AuthorizationPageForgotPwLocators


# Page Object class for Authorization page
class AuthorizationPage(BasePage):
    def __init__(self, webdriver, logger):
        super().__init__(webdriver=webdriver, logger=logger)

    """
    REGISTRATION BLOCK--------------------------------------------------------------------------------------------------
    """

    # Email field of Registration block
    @property
    def email_field_reg(self):
        try:
            self.logger.debug(f"Searching for email field by {AuthorizationPageRegistrationLocators.EMAIL_FIELD_REG.value}")
            return self.wait.until(EC.element_to_be_clickable(AuthorizationPageRegistrationLocators.EMAIL_FIELD_REG.value))
        except TimeoutError as te:
            self.logger.error(f"Email field not found!")

    # Create account button of Registration block
    @property
    def create_account_button_reg(self):
        return self.wait.until(
            EC.element_to_be_clickable(AuthorizationPageRegistrationLocators.CREATE_ACCOUNT_BUTTON_REG.value))

    # Function enters provided email into email field and clicks on create account button (Registration block)
    @step("Fill out email into email field")
    def signup(self, email: str):
        self.logger.debug(f"Sending keys to email field..")
        self.actions \
            .send_keys_to_element(self.email_field_reg, email) \
            .pause(2) \
            .perform()

    # Error block which is displayed after unsuccessful providing email
    @property
    def create_account_error_block(self):
        return self.wait.until(
            EC.visibility_of_element_located(AuthorizationPageRegistrationLocators.CREATE_ACCOUNT_ERROR_BLOCK.value))

    """
    SIGN IN BLOCK ------------------------------------------------------------------------------------------------------
    """

    # Email field of Sign in block
    @property
    def email_field_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.EMAIL_FIELD_SIGNIN.value))

    # Create account button of Sign in block
    @property
    def create_account_button_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.CREATE_BUTTON_SIGNIN.value))

    # Sign in button of Sign in block
    @property
    def sign_in_button(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageSignInLocators.SIGN_IN_BUTTON.value))

    # Forgot pw button of Sign in block
    @property
    def forgot_pw(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.FORGOT_PW.value))

    """
    FORGOT PW BLOCK--------------------------------------------------------------------------------------------------
    """

    # Email field of Forgot pw block
    @property
    def email_forgot_pw(self):
        return self.wait.until(
            EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.EMAIL_FIELD_FORGOT_PW.value))

    # Confirm email button of Forgot pw block
    @property
    def confirm_email_forgot_pw_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(AuthorizationPageForgotPwLocators.CONFIRM_EMAIL_FORGOT_PW_BUTTON.value))

    # Success message block after email entered of Forgot pw block
    @property
    def alert_success_block(self):
        return self.wait.until(
            EC.presence_of_element_located(AuthorizationPageForgotPwLocators.ALERT_SUCCESS_BLOCK.value))

    # Function enters provided email and confirms (Forgot pw block)
    @step("Fill out email into email field")
    def enter_email_forgot_pw(self, email: str):
        self.logger.debug(f"Sending keys to email forgot pw field..")
        self.actions.send_keys_to_element(self.email_forgot_pw, email).pause(1).perform()
