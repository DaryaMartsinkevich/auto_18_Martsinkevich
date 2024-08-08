import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from lesson19.helpers import add_cookie

URL = 'https://testpages.eviltester.com/styled/cookies/adminview.html'

@pytest.fixture()
def driver_firefox():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_assert_cookies(driver_firefox):
    driver_firefox.get(URL)

    driver_firefox.find_element(By.CSS_SELECTOR, '[id="username"]').send_keys('Admin')
    driver_firefox.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys('AdminPass')
    driver_firefox.find_element(By.CSS_SELECTOR, '[id="login"]').click()

    time.sleep(1)

    cookies = driver_firefox.get_cookies()
    assert cookies[0]['value'] == 'Admin'
    assert cookies[0]['name'] == 'loggedin'

def test_get_cookie(driver_firefox):
    driver_firefox.get(URL)

    driver_firefox.find_element(By.CSS_SELECTOR, '[id="username"]').send_keys('Admin')
    driver_firefox.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys('AdminPass')
    driver_firefox.find_element(By.CSS_SELECTOR, '[id="login"]').click()

    time.sleep(1)

    cookie = driver_firefox.get_cookie('loggedin')
    assert cookie['value'] == 'Admin'
    assert cookie['name'] == 'loggedin'

def test_add_cookie(driver_firefox):
    driver_firefox.get(URL)
    add_cookie(driver_firefox, 'loggedin', 'Admin')
    driver_firefox.refresh()

    time.sleep(1)

    assert driver_firefox.find_element(By.XPATH, '/html/body/div/div[2]')

def test_delete_cookie(driver_firefox):
    driver_firefox.get(URL)
    add_cookie(driver_firefox, 'loggedin', 'Admin')
    driver_firefox.refresh()

    time.sleep(1)

    assert driver_firefox.find_element(By.XPATH, '/html/body/div/div[2]')
    driver_firefox.save_screenshot('test_delete_cookie1.png')
    driver_firefox.delete_all_cookies()
    driver_firefox.refresh()

    time.sleep(2)
    assert driver_firefox.find_element(By.CSS_SELECTOR, '[id="username"]')
    assert driver_firefox.find_element(By.CSS_SELECTOR, '[id="password"]')
    assert driver_firefox.find_element(By.CSS_SELECTOR, '[id="login"]')

    driver_firefox.save_screenshot('test_delete_cookie2.png')

