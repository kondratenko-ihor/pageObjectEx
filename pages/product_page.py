from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_price()
        # self.should_be_product_url()
        self.basket_button_should_be_visible()


    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url, "`promo=newYear` is not presented in the link"
        assert True

    def basket_button_should_be_visible(self):
        assert len(ProductPageLocators.ADD_TO_BASKET_BUTTON) > 0, "Basket button is not presented"
        assert True

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert True

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_price(self):
        BASKET_PRICE = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        PRODUCT_PRICE = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert BASKET_PRICE.text == PRODUCT_PRICE.text, "Prices not the same"

    def check_product_name_in_basket(self):
        PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        PRODUCT_IN_BASKET = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert PRODUCT_NAME.text == PRODUCT_IN_BASKET.text, "names not the same(((("

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
           "Success message is presented, but should not be"

    def message_should_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
            "Success message should disappear"

