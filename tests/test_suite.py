import allure
import requests

from pages.api_keys import ApiKeysPage
from pages.home import HomePage
from pages.main import MainPage
from pages.sign_in import SignInPage


@allure.suite('Test')
class TestSuite:
    @allure.feature('Save API Key to the file')
    def test_save_api_key_to_the_file(self, browser):
        # Set up test case data
        EMAIL = 'ivanponomarchuk1@gmail.com'
        PASSWORD = 'Test12345'
        NOTICE = 'Signed in successfully.'

        with allure.step('Open browser and navigate to the OpenWeather main page'):
            main_page = MainPage(browser)
            main_page.load()
        with allure.step('Click "Sign In" link'):
            main_page.click_sign_in_link()
        with allure.step('Sign in with email and password'):
            sign_in_page = SignInPage(browser)
            sign_in_page.sign_in(EMAIL, PASSWORD)
        with allure.step('Verify that "Logout" link is visible'):
            home_page = HomePage(browser)
            home_page.verify_logout_link_is_visible()
        with allure.step('Verify that right notice is displayed'):
            assert home_page.get_notice_text() == NOTICE
        with allure.step('Click on "API Keys" tab'):
            home_page.click_api_keys_tab()
        with allure.step('Save API Key to the file'):
            api_keys_page = ApiKeysPage(browser)
            api_keys_page.save_api_key_to_the_file()

    @allure.feature('Get weather for location')
    def test_get_weather_for_location(self, get_api_key):
        # Set up test case data
        URL = "https://api.openweathermap.org/data/2.5/forecast"
        LOCATION_ID = 698740
        PARAMS = {'id': LOCATION_ID, 'appid': get_api_key}

        with allure.step('Send GET request with parameters'):
            response = requests.get(URL, PARAMS)
        with allure.step('Validate response code'):
            assert response.status_code == 200
        with allure.step('Get list with descriptions of weather'):
            data = response.json()
            weather = [item["weather"][0]['description'] for item in data["list"]]
        with allure.step('Check that weather will be partly cloudy'):
            assert "few clouds" in weather
