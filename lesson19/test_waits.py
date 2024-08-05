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
    yield driver

    driver.close()
    driver.quit()

def test_no_wait(driver_firefox):
    driver_firefox.get(URL)

    assert driver_firefox.find_element(By.XPATH, '//*[@id="ensModalWrapper"]/div')

def test_audi_implicitly_wait(driver_firefox):
    driver_firefox.implicitly_wait(5)
    driver_firefox.get(URL)

    assert driver_firefox.find_element(By.XPATH, '//*[@id="ensModalWrapper"]/div')

def test_audi_time_sleep(driver_firefox):
    time.sleep(5)
    driver_firefox.get(URL)

    assert driver_firefox.find_element(By.XPATH, '//*[@id="ensModalWrapper"]/div')
