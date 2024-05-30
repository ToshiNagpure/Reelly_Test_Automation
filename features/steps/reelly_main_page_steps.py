from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


EMAIL_INPUT = (By.ID,"email-2")
PASSWORD_INPUT= (By.CSS_SELECTOR, "input[data-name='Password']")
LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button w-button']")
SETTINGS_MENU=(By.XPATH,"//div[text()='Settings']")
SETTING_PAGE=(By.CSS_SELECTOR,"body[class='body-setting']")
OPTIONS_MENU=(By.CSS_SELECTOR,"a[class*='page-setting-block w-inline-block']")
CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")


@given("Open the main page")
def open_reelly(context):
    context.app.main_page.open_main_page()


@when('Log in to the page')
def login(context):
     context.driver.find_element(*EMAIL_INPUT).send_keys("roshni.mohare@gmail.com")
     context.driver.find_element(*PASSWORD_INPUT).send_keys("Pass@word1")
     context.driver.find_element(*LOGIN_BUTTON).click()
     sleep(3)


@when('Click on settings option')
def click_settings(context):
    context.driver.find_element(*SETTINGS_MENU).click()


@then ('Verify the right page opens')
def verify_settings(context):
    context.driver.find_element(*SETTING_PAGE)


@then ('Verify there are 11 options for the settings')
def verify_setting_options(context):
    options = context.driver.find_elements(*OPTIONS_MENU)
    print(options)
    assert len(options) == 12, f' Expected 11 links but found {len(options)}'


@then ('Verify “connect the company” button is available')
def verify_company_button(context):
    context.driver.find_element(*CONNECT_THE_COMPANY_BTN)