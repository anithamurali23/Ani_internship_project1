from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



@given('Open the main page')
def open_main_page(context):
    context.app.login_page.login_pages()


@when('Log in to the page')
def log_in_to_page(context):
    context.app.login_page.click_on_signin_link()
    sleep(2)
    context.app.login_page.input_email("anithaprakash@gmail.com")
    sleep(2)
    context.app.login_page.input_password("colorblue23")
    sleep(2)
    context.app.login_page.click_continue_button()

@then('Click on Get a free subscription')
def click_free_subscription(context):
    context.app.main_screen_page.get_subscription_click()


@then('Switch the new tab')
def new_page_open(context):
    context.app.subscription_page.open_new_page()


@then('Verify the {text} in the new tab')
def verify_free_subscription_text(context, text):
    context.app.subscription_page.verify_subscription_text(text)

