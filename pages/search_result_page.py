from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    BUTTON_FOR_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
    SUB_TOTAL_BTN = (By.CSS_SELECTOR, '#sc-subtotal-label-buybox')
    GOTO_CART_PAGE = (By.CSS_SELECTOR, '[href="/cart?ref_=sw_gtc"]')

    def verify_search_result(self, result):
        self.verify_text(result, *self.SEARCH_RESULT)

    def verifying_empty_cart(self,text):
        self.verify_text(text,*self.EMPTY_CART_TEXT)

    def verify_item(self,text):
        self.verify_text(text,*self.SUB_TOTAL_BTN)

    def click_add_to_the_cart(self):
        self.click(*self.BUTTON_FOR_ADD_TO_CART)
        self.click(*self.GOTO_CART_PAGE)



