import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

URL_1 = 'https://www.reddit.com'
URL_2 = 'https://www.youtube.com'
URL_3 = 'https://testpages.eviltester.com/styled/index.html'

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()

def test_get_info_about_page(driver):
    driver.get(URL_1)
    time.sleep(1)

    assert URL_1 in driver.current_url
    assert driver.title == 'Reddit - Dive into anything'
    assert driver.page_source


def test_page_find_element(driver):
    driver.get(URL_3)

    element = driver.find_element(By.ID, "basicpagetest")
    element.click()
    element_1 = driver.find_element(By.XPATH, '/html/body/div/h1')
    time.sleep(2)
    assert element_1

    element_2 = driver.find_element(By.CSS_SELECTOR, ".main")
    time.sleep(2)
    assert element_2

    element_3 = driver.find_element(By.CSS_SELECTOR, ".sub")
    time.sleep(2)
    assert element_3
