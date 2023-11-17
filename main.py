from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time as time

chrome_driver_path = 'C:/Users/hugo_/OneDrive/Área de Trabalho/chromedriver_win32/chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

#----------------------------FUNÇÕES----------------------------

def verificaLogin():
    try:
        

#----------------------------APP----------------------------

driver.get('https://www.linkedin.com')
time.sleep(60)
print("Vou Verficar o Login")
verificaLogin()
print("verificado")
time.sleep(10)

