from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):

    EMAIL_INPUT = (By.ID, "email-2")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-name='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button w-button']")

    def login(self, email, password):
        self.input_text(email,*self.EMAIL_INPUT)
        self.input_text(password,*self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)


