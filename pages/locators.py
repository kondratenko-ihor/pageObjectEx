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

class ProductPageLocators(BasePage):
    ADD_TO_BASKET_BUTTON = (By.ID, "add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    LINK_PRODUCT_PAGE = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner  > p > strong")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) > .alertinner  > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")