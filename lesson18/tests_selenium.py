import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.selenium.dev/'


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-search-engine-choice-screen")
    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")
    chrome_service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()
    yield driver

    # driver.close()
    driver.quit()

def test_selenium_assert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '.selenium-button.selenium-webdriver')
    element.click()
    time.sleep(2)

    assert driver.current_url == 'https://www.selenium.dev/documentation/webdriver/'

    driver.close()
    driver.quit()

