# фикстура
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from settings import HEADLESS


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080")

    if HEADLESS:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-popup-blocking")
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # chrome_options.add_experimental_option("prefs", prefs)

    cap = DesiredCapabilities.CHROME
    cap = {
        "browserName": "chrome",
        "browserVersion": "80.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://192.168.166.115:4444/wd/hub",
        desired_capabilities=cap)

    driver.set_page_load_timeout(60)
    print(driver.get_window_size())
    yield driver
    driver.quit()