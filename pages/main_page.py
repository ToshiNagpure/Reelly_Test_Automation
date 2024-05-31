from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    SETTINGS_MENU_ANCHOR_LINK = (By.XPATH, "//a[contains(@href,'/settings')]")

    def open_settings(self):
        self.click(*self.SETTINGS_MENU_ANCHOR_LINK)