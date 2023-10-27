from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger

# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/test/get_free_subscription

def browser_init(context):
#  def browser_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """

    service = Service(executable_path='/Users/anithamurali/Desktop/Anitha_Internship_project 2/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    options = webdriver.ChromeOptions()
    mobile_emulation = {
             "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
             "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }
    options.add_experimental_option("mobileEmulation",mobile_emulation)
    options.add_argument("--lig-level=3")
    context.driver = webdriver.Chrome(options=options,service=service)
    context.driver.set_window_size(500, 950)
    context.driver.get('https://soft.reelly.io/sign-up')


    # service = Service(executable_path='//Users/anithamurali/Downloads/Anitha_Internship_project/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path='//Users/anithamurali/Downloads/Anitha_Internship_project/chromedriver')
    #
    # context.driver = webdriver.Chrome(options=options, service=service)
    # context.driver.set_window_size(1920,1080)
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()


    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#     bs_user = 'anithaprakash_Hemdkb'
#     bs_key = 'Qars2pwqkMUGxRPfXZGA'
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#
#     options = Options()
#     bstack_options = {
#     'os': "OS X",
#     'osVersion': "Ventura",
#     'browserName': "Chrome",
#     'sessionName': "scenario_name"
# }
#     options.set_capability('bstack:options', bstack_options)
#     context.driver = webdriver.Remote(command_executor=url, options=options)


    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    # browser_init(context,scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
