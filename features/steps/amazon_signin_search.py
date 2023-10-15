from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
FOOTER_LINKS = (By.CSS_SELECTOR,'.navFooterDescItem')


@given('Open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()

@when('click Returns and Orders')
def click_returns(context):
    context.app.header.returns_orders()

@when('Click on button from SignIn popup')
def signin_btn_click(context):
    context.app.header.click_signin_from_popup()

@then('Verify Sign in page opens')
def go_to_signin_page(context):
    context.app.signin_page.verify_signin_opened()


@then('Verify Sign in is clickable')
def click_signin_page(context):
    context.app.header.verify_signin_btn_clickable()

@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)

@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()

@then('Verify Sign In disappears')
def signin_disappear(context):
    context.app.header.verify_signin_btn_disappears()

@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1, f'Expected at least 2 links, but got {len(links)}'


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()

# @then('email input field is present')
# def email_field_present(context):
#     context.app.header.email_input()