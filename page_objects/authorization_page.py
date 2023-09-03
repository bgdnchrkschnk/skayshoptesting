from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import *
from locators.pages_obj.authorization_page import AuthorizationPageLocators


class AuthorizationPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver)

    """
    REGISTRATION BLOCK--------------------------------------------------------------------------------------------------
    """

    @property
    def email_field_reg(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.EMAIL_FIELD_REG.value))


    @property
    def create_account_button_reg(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.CREATE_ACCOUNT_BUTTON_REG.value))

    def signup(self, email: str):
        self.actions.\
            send_keys_to_element(email, element=self.email_field_reg).\
            click(on_element=self.create_account_button_reg).perform()

    """
    SIGN IN BLOCK ------------------------------------------------------------------------------------------------------
    """

    @property
    def email_field_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.EMAIL_FIELD_SIGNIN.value))


    @property
    def create_account_button_signin(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.CREATE_BUTTON_SIGNIN.value))


    @property
    def sign_in_button(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.SIGN_IN_BUTTON.value))


    @property
    def forgot_pw(self):
        return self.wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.FORGOT_PW.value))



