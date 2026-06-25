from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pytest
import time


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=498,870")
    mobile_emulation = {'deviceName': 'iPhone 12 Pro'}

    options.add_experimental_option('mobileEmulation', mobile_emulation)
                              
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.twitch.tv/')

    try:
        yield driver
    except Exception as e:
        raise ValueError(str(e))
    finally:
        driver.quit()
