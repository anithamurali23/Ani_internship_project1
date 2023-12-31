from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#create a new Chrome browser instance
service = Service(executable_path="/Users/anithamurali/Desktop/python-selenium-automation1/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('http://www.amazon.com/')

driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList').click()
driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'#ap_email').click()
driver.find_element(By.CSS_SELECTOR,'#ap_password').click()
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'#continue')
driver.find_element(By.CSS_SELECTOR,'[href*="gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?"]')
driver.find_element(By.CSS_SELECTOR,'[href*="gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?"]')
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age']")





