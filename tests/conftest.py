import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome(executable_path=r"resources\chromedriver.exe")
    driver.fullscreen_window()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()


@pytest.fixture
def get_api_key():
    # Read API Key from file
    file = open(r'resources\keys.txt', 'r')
    API_KEY = file.read()
    yield API_KEY
    file.close()
