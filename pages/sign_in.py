from selenium.webdriver.common.by import By

from pages.base import BasePage


class SignInPage(BasePage):
    EMAIL_INPUT = (By.ID, 'user_email')
    PASSWORD_INPUT = (By.ID, 'user_password')
    SUBMIT_BUTTON = (By.NAME, 'commit')

    def sign_in(self, email, password):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()
