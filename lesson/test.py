import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # безголовый реж
options.add_argument("--window-size=1920x1080") # Запуск браузера с заданным разрешением
options.add_argument("--disable-blink-features=AutomationControlled") # Отключение средства автоматизации т.е. браузером управляет человек
# подмена user-agenta
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait =WebDriverWait(driver,5,poll_frequency=1)

driver.get("https://www.otpusk.com/search/egypt/")
#driver.save_screenshot("screenshot.png") # скриншот
time.sleep(5)