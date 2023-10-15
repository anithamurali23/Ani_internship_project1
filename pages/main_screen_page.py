from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep



class MainScreenPage(Page):

    GET_SUBSCRIPTION= (By.CSS_SELECTOR, ".get-free-period.menu")


    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(3)
        self.driver.refresh()

    def get_subscription_click(self):
        self.click(*self.GET_SUBSCRIPTION)
        sleep(3)


    def store_original_window(self):
        return self.get_current_window()