from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    SETTINGS_MENU_ANCHOR_LINK = (By.XPATH, "//a[contains(@href,'/settings')]")
    SETTINGS_MENU_ANCHOR_LINK_MOBILE_LOCATOR = (By.XPATH, "//div[@class='mobile-top-menu']")

    def open_settings(self):
        # choose the locator based on browser emulation setting
        if self.is_mobile_emulation:
            self.click(*self.SETTINGS_MENU_ANCHOR_LINK_MOBILE_LOCATOR)
        else:
            self.click(*self.SETTINGS_MENU_ANCHOR_LINK)