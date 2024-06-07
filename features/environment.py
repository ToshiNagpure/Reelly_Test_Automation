from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options

def browser_init(context, scenario_name="Reelly_Test_Automation"):
    """
    This method is used to initialize the browser instance
    :param context: Context of the scenario
    :param scenario_name: Name of the scenario
    """

    bs_user = 'roshnimohare_isEGeR'
    bs_ak = '7yR2bkMLxbspa3pRjfEB'
    url = f'http://{bs_user}:{bs_ak}@hub-cloud.browserstack.com/wd/hub'

    bstack_options = {
        'browser': 'Chrome',
        'os': 'Windows',
        'sessionName': scenario_name
    }
    options = Options()
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
