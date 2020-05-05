from selenium.webdriver.common.by import By
from .locators import MainPageLocators, LoginPageLocators
from selenium import webdriver
from .base_page import BasePage
from .login_page import LoginPage


# Класс  MainPage нужно сделать наследником класса BasePage.
# Класс-предок в Python указывается в скобках:
# Таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    def go_to_login_page(self):  # В аргументы больше не надо передавать экземпляр браузера,
        # мы его передаем и сохраняем на этапе создания Page Object.
        # Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)  # т.к браузер хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью
        login_link.click()

    def should_be_logic_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"