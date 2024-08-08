import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from lesson19.helpers import add_cookie

URL = 'https://www.youtube.com'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_find_element(driver):
    assert driver.find_element(By.CSS_SELECTOR, '[id="content-wrapper"]')


def test_find_elements(driver):
    driver.get(URL)
    assert len(driver.find_elements(By.CSS_SELECTOR, '[id="content-wrapper"]')) == 1


def test_text(driver):
    driver.get(URL)
    el = driver.find_element(By.CSS_SELECTOR, '[id="content-wrapper"]')
    assert el.text == 'Попробуйте найти что-нибудь\nНачните смотреть видео, и мы подберем для вас рекомендации.'


def test_get_attribute(driver):
    driver.get(URL)
    driver.implicitly_wait(5)
    el = driver.find_element(By.CSS_SELECTOR, '[id="content-wrapper"]')
    assert el.get_attribute('class') == 'style-scope ytd-feed-nudge-renderer'

    assert el.get_attribute('disabled') == None


def test_value_of_css_property(driver):
    driver.get(URL)
    driver.implicitly_wait(5)
    el = driver.find_element(By.CSS_SELECTOR, '[id="content-wrapper"]')
    assert el.value_of_css_property('background-color') == 'rgba(255, 255, 255, 1)'