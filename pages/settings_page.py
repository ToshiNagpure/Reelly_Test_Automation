from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class SettingsPage(BasePage):

    SETTINGS_PAGE = (By.CSS_SELECTOR, "body[class='body-setting']")
    SETTINGS_OPTIONS_MENU = (By.CSS_SELECTOR, "a[class*='page-setting-block w-inline-block']")
    SETTINGS_CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")

    def verify_setting_page(self):
        self.find_element(*self.SETTINGS_PAGE)

    def get_options_link(self):
        return self.find_elements(*self.SETTINGS_OPTIONS_MENU)

    def verify_company_button(self):
        return self.find_element(*self.SETTINGS_CONNECT_THE_COMPANY_BTN)