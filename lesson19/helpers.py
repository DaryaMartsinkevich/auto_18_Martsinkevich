def add_cookie(driver, name, value):
    cookie = {'name': name, 'value': value}
    driver.add_cookie(cookie)