from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not presented in url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_FIELD), "e-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_FIELD), "password field is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "register form is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER_FIELD), "password field is not presented"
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER_FIELD), "email field is not presented"
        assert True

    def fill_in_login_form_valid(self):
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN_FIELD).send_keys(*LoginPageLocators.VALID_EMAIL)
        self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_FIELD).send_keys("LoginPageLocators")

    def fill_in_login_form_invalid(self):
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN_FIELD).send_keys(*LoginPageLocators.VALID_EMAIL)
        self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_FIELD).send_keys("выавыаываыва")