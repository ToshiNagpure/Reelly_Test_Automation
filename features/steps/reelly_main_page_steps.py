from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


MAIN_PAGE_URL = "https://soft.reelly.io/sign-in"
SIGNIN_EMAILADDRESS = "tn.testuser100@gmail.com"
SIGNIN_PASSWORD = "ABC123"

@given("Open the main page")
def open_main_page(context):
    context.app.main_page.open(MAIN_PAGE_URL)

@when('Log in to the page')
def signin(context):
    context.app.sign_in_page.login(SIGNIN_EMAILADDRESS, SIGNIN_PASSWORD)


@when('Click on settings option')
def open_settings(context):
    context.app.main_page.open_settings()


@then ('Verify the right page opens')
def verify_settings(context):
    context.app.settings_page.verify_setting_page()


@then ('Verify there are 11 options for the settings')
def verify_setting_options(self):
    options = self.app.settings_page.get_options_link()
    print(options)
    assert len(options) == 12, f' Expected 11 links but found {len(options)}'


@then ('Verify “connect the company” button is available')
def verify_company_button(context):
    context.app.settings_page.verify_company_button()