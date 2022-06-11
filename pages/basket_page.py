from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def basket_should_not_contain_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "There is a basket summary block on the page."
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "There is a basket item on the page."

    def should_have_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "There is no BASKET_IS_EMPTY message in the page."