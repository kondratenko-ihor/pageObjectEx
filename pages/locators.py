from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "[name='login-username']")
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "[name='login-password']")
    REGISTER_FROM = (By.ID, "register_form")
    EMAIL_REGISTER_FIELD = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_REGISTER_FIELD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    VALID_EMAIL = ("correct email")

