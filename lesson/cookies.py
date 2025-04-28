import os
import time
import pytest
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_demoqa_form():
    options = Options()
    #options.add_argument('--headless') # безголовый реж
    #options.add_argument("--window-size=1920x1080") # Запуск браузера с заданным разрешением
    options.add_argument("--disable-blink-features=AutomationControlled") # Отключение средства автоматизации т.е. браузером управляет человек
    # подмена user-agenta
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait =WebDriverWait(driver,5,poll_frequency=1)

    try:
        #driver.get("https://www.amazon.com/")
        # time.sleep(4)
        #
        # before = driver.get_cookie("session-id") #Вернет куку name или любую другую указанную в качестве аргумента
        # print(before)
        #
        # driver.delete_cookie("session-id")
        #
        # driver.add_cookie({                   #Добавление Cookies
        #     "name":"session-id",
        #     "value": "hi"
        # })
        #
        # after = driver.get_cookie("session-id")
        # print(after)
        driver.get("https://www.instagram.com/?flo=true")
        # time.sleep(2)
        # name = driver.find_element("xpath","//input[@name='username']")
        # name.send_keys("apofiosis79@gmail.com")
        # time.sleep(2)
        # password = driver.find_element("xpath", "//input[@name='password']")
        # password.send_keys("1bender1$AureolA!627$")
        # time.sleep(2)
        #
        # enter = driver.find_element("xpath", "//button[@type='submit']")
        # enter.click()
        # time.sleep(30)
        #
        # pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl",'wb'))  #сохранением куков в файл, для этого в библиотеке pickle есть метод dump
        driver.delete_all_cookies()

        cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl",'rb')) # После этого, считаем из файла с куками все данные и запишем в переменную с помощью метода pickle.load

        for cookie in cookies:
              driver.add_cookie(cookie)

        time.sleep(5)
        driver.refresh()
        time.sleep(5)
    finally:
        driver.quit()