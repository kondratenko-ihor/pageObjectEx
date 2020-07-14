from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


# @pytest.mark.smoke
def test_guest_can_add_product_to_basket(browser):
    link = (ProductPageLocators.LINK_PRODUCT_PAGE)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price()
    page.check_product_name_in_basket()

@pytest.mark.parametrize('link2', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"])
def test_guest_can_add_product_to_basket(browser, link2):
    url = f"{link2}"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price()
    page.check_product_name_in_basket()


@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_should_disappeared()