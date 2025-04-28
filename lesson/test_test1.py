import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def test_your_function():
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 5, poll_frequency=1)
# options = Options()
# options.add_argument('--headless') # безголовый реж
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome( service=service)
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait =WebDriverWait(driver,5,poll_frequency=1)

    driver.get("https://demoqa.com/text-box")

    time.sleep(3)

    Full_name = driver.find_element("xpath","//input[@placeholder='Full Name']")

    assert Full_name.get_attribute("value")==""

    Full_name.send_keys("Igor")
    value = Full_name.get_attribute("value") # создаём переменную value и получаем значение из input-поля
    assert "Igor" in value # Проверяем что "Igor" есть в значение value
    print(value) # выводим значения

    time.sleep(3)

    email_name = driver.find_element("xpath","//input[@placeholder='name@example.com']")

    assert email_name.get_attribute("value")==""

    email_name.send_keys("qwer@.com")

    time.sleep(3)

    Current_Address = driver.find_element("xpath","//textarea[@placeholder='Current Address']")

    Current_Address.send_keys("Street krolevec 62")
    value1 = Current_Address.get_attribute("value") # Получаем значение из input-поля
    assert "Street krolevec 62"== value1
    print(value1)
    time.sleep(3)

    Permanent_Address = driver.find_element("xpath","//textarea[@id='permanentAddress']")

    Permanent_Address.send_keys("adrrees 2")

    time.sleep(3)

    driver.get("https://the-internet.herokuapp.com/status_codes")

    Code_200 = driver.find_element("xpath","//a[@href='status_codes/200'] ")
    time.sleep(3)
    Code_200.click()

    time.sleep(3)

    driver.back()

    driver.quit()