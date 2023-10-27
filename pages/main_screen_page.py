from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep



class MainScreenPage(Page):

    GET_SUBSCRIPTION= (By.CSS_SELECTOR, ".get-free-period.menu")
    MENU_BUTTON = (By.XPATH, '//div[text()="Menu"][@class="mobile-top-menu"]')
    CONNECT_THE_COMPANY_BUTTON = (By.XPATH,'/html/body/div[3]/div[2]/a[1]/div')


    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(3)
        self.driver.refresh()

    def click_menu_button(self):
        self.wait_for_element_clickable_click(*self.MENU_BUTTON)


    def click_connect_the_company(self):
        self.wait_for_element_clickable_click(*self.CONNECT_THE_COMPANY_BUTTON)


    def store_original_window(self):
        return self.get_current_window()