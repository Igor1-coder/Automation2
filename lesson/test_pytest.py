import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


def test_demoqa_form():
    options = Options()
    options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 5, poll_frequency=1)

    try:
        driver.get("https://demoqa.com/text-box")
        time.sleep(3)

        Full_name = driver.find_element("xpath", "//input[@placeholder='Full Name']")
        assert Full_name.get_attribute("value") == ""

        Full_name.send_keys("Igor")
        value = Full_name.get_attribute("value")
        assert "Igor" in value
        print(value)

        email_name = driver.find_element("xpath", "//input[@placeholder='name@example.com']")
        assert email_name.get_attribute("value") == ""

        email_name.send_keys("qwer@.com")

        Current_Address = driver.find_element("xpath", "//textarea[@placeholder='Current Address']")
        Current_Address.send_keys("Street krolevec 62")
        value1 = Current_Address.get_attribute("value")
        assert "Street krolevec 62" == value1
        print(value1)

        Permanent_Address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
        Permanent_Address.send_keys("adrrees 2")

        driver.get("https://the-internet.herokuapp.com/status_codes")
        Code_200 = driver.find_element("xpath", "//a[@href='status_codes/200']")
        Code_200.click()

        driver.back()

    finally:
        driver.quit()