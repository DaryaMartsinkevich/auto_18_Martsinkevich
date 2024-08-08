import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from lesson19.helpers import add_cookie

URL_1 = 'https://demoqa.com/automation-practice-form'
URL_2 = 'https://www.youtube.com'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_fill_form(driver):
    driver.get(URL_1)

    name = driver.find_element(By.CSS_SELECTOR, '[id="firstName"]')
    male = driver.find_element(By.CSS_SELECTOR, '[class="custom-control custom-radio custom-control-inline"]')
    female = driver.find_elements(By.CSS_SELECTOR, '[class="custom-control custom-radio custom-control-inline"]')[1]
    sport = driver.find_elements(By.CSS_SELECTOR, '[class="custom-control custom-checkbox custom-control-inline"]')[0]
    reading = driver.find_elements(By.CSS_SELECTOR, '[class="custom-control custom-checkbox custom-control-inline"]')[1]
    file = driver.find_element(By.CSS_SELECTOR, '[type="file"]')
    submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    city = driver.find_element(By.CSS_SELECTOR, '[class="col-md-4 col-sm-12"]')

    lastName = driver.find_element(By.CSS_SELECTOR, '[id="lastName"]')
    userNumber = driver.find_element(By.CSS_SELECTOR, '[id="userNumber"]')

    name.send_keys('qwertg')
    lastName.send_keys('qwertg')
    userNumber.send_keys('1234564545')
    male.click()
    sport.click()
    reading.click()
    file.send_keys('/Users/elenayanushevskaya/teachmeskills/auto_18/lesson19/test_2.png')

    assert lastName.is_displayed()
    assert male.is_selected()
    assert not female.is_selected()
    assert sport.is_selected()
    assert reading.is_selected()
    assert city.is_displayed()
    assert not city.is_enabled()