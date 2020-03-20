from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):
    LOGOUT_LINK = (By.XPATH, '//a[contains(text(),"Logout")]')
    NOTICE = (By.XPATH, '//div[@class="panel-body"]')
    API_KEYS_TAB = (By.XPATH, '//a[contains(text(),"API keys")]')

    def verify_logout_link_is_visible(self):
        logout_link = self.browser.find_element(*self.LOGOUT_LINK)
        logout_link.is_displayed()

    def get_notice_text(self):
        notice = self.browser.find_element(*self.NOTICE)
        return notice.text

    def click_api_keys_tab(self):
        api_keys_tab = self.browser.find_element(*self.API_KEYS_TAB)
        api_keys_tab.click()
