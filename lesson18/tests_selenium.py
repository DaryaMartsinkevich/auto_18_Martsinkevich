import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

    driver.close()
    driver.quit()

def test_selenium_assert(driver):

    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '[class="d-flex justify-content-center td-box--100 pt-5"]')
    assert element

    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView()", element)

    element = driver.find_element(By.XPATH, "//*[@class='selenium-button-container']")
    assert element

    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.save_screenshot('selenium.png')
    assert driver.current_url == 'https://www.selenium.dev/documentation/webdriver/'


