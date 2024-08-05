import time

import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
URL = 'https://www.audi.com/en.html'

@pytest.fixture()
def driver_firefox():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()


def test_audi(driver_firefox):
    driver_firefox.get(URL)
    time.sleep(3)
    assert driver_firefox.find_element(By.XPATH, '//*[@id="ensModalWrapper"]/div')
