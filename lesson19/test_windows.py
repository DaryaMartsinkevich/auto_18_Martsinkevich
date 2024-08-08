import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


URL = 'https://www.youtube.com'

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()

def test_windows_handles(driver):
    driver.get(URL)

    driver.find_element(By.CSS_SELECTOR, '[id="content-wrapper"]')
    time.sleep(3)
    assert len(driver.window_handles) == 2


