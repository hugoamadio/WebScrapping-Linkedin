from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as time

chrome_driver_path = 'C:/Users/hugo_/OneDrive/Área de Trabalho/chromedriver_win32/chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('https://www.linkedin.com')
time.sleep(5)
print("Site Carregado")
time.sleep(1)
inputEmail = driver.find_element(By.ID, 'session_key')
time.sleep(1)
inputEmail.send_keys('hugo_amadio@hotmail.com')
time.sleep(1)
inputKey = driver.find_element(By.ID,'session_password')
time.sleep(1)
inputKey.send_keys('senha')
time.sleep(1)

# btnEntrar = driver.find_element(By.CSS_SELECTOR, '.btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width').text
time.sleep(70)