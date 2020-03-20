from selenium.webdriver.common.by import By

from pages.base import BasePage


class ApiKeysPage(BasePage):
    API_KEY = (By.XPATH, '//table[@class="table api-keys"]//tbody/tr/td/pre')

    def save_api_key_to_the_file(self):
        api_key = self.browser.find_element(*self.API_KEY).text
        # Write API Key to file
        file = open(r'resources\keys.txt', 'w')
        file.write(api_key)
        file.close()
