from selenium.webdriver.common.by import By

from .base_page import BasePage

# Класс  MainPage нужно сделать наследником класса BasePage.
# Класс-предок в Python указывается в скобках:
# Таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
# В аргументы больше не надо передавать экземпляр браузера,
# мы его передаем и сохраняем на этапе создания Page Object.
# Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
# т.к браузер хранится как аргумент класса BasePage,
# обращаться к нему нужно соответствующим образом с помощью
