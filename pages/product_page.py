from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_add_product_to_basket_and_show_basket_total(self):
        self.should_be_product_page()
        self.add_product_to_basket()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.check_that_product_was_added_to_basket(product_name, product_price)

    def should_be_product_page(self):
        self.should_have_product_description()
        self.should_have_price()

    def add_product_to_basket(self):
        self.should_have_add_to_basket_button()
        self.click_on_add_to_basket_button()
        self.solve_quiz_and_get_code()

    def check_that_product_was_added_to_basket(self, product_name, product_price):
        self.should_see_that_product_has_been_added_to_basket(product_name)
        self.should_have_correct_basket_total_value(product_price)

    def should_have_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "\"Add to basket\" button is not present."

    def should_have_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price is not present."

    def should_have_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present."

    def click_on_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_see_that_product_has_been_added_to_basket(self, product_name):
        # Not sure what is expected exactly. Message might be shown not only in English, so we check displaying product name here
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_THE_INNER_ALERT), "There is no product name in the inner alert."
        product_name_in_the_inner_alert = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_THE_INNER_ALERT).text
        assert product_name == product_name_in_the_inner_alert, f"[\"{product_name}\"] is shown as [\"{product_name_in_the_inner_alert}\"] in the inner alert."

    def should_have_correct_basket_total_value(self, product_price):
        # Not sure what is expected exactly. Message might be shown not only in English, so we check displaying basket total here
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_IN_THE_INNER_ALERT), "There is no basket total in the inner alert."
        price_in_the_inner_alert = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_IN_THE_INNER_ALERT).text
        assert product_price == price_in_the_inner_alert, f"[\"{product_price}\"] is shown as [\"{price_in_the_inner_alert}\"] in the inner alert."

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_THE_INNER_ALERT), \
            "There is a \"SUCCESSFULLY_ADDED\" inner alert on the page."

    def should_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_THE_INNER_ALERT), \
            "There is no \"SUCCESSFULLY_ADDED\" inner alert on the page."

    def should_have_success_message_disappeared(self):
        assert self.is_element_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_THE_INNER_ALERT), \
            "\"SUCCESSFULLY_ADDED\" inner alert didn't disappear in time."
