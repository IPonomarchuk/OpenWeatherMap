from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):
    URL = 'https://openweathermap.org/'
    SIGN_IN_LINK = (By.XPATH, '//a[contains(@class,"pull-right")][contains(text(),"Sign In")]')

    # Navigate to the OpenWeather main page
    def load(self):
        self.browser.get(self.URL)

    def click_sign_in_link(self):
        sign_in_link = self.browser.find_element(*self.SIGN_IN_LINK)
        sign_in_link.click()
