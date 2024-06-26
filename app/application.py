from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.signIn_page import SignInPage
from pages.settings_page import SettingsPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.base_page = BasePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.settings_page = SettingsPage(driver)
