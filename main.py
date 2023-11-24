from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as time
import tkinter as tk

#-------------------------------------------------------------------------------------------------------

def logar(email, senha):
    chrome_driver_path = 'C:/Users/hugo_/OneDrive/Área de Trabalho/chromedriver_win32/chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.linkedin.com')
    time.sleep(5)
    print("Site Carregado")
    time.sleep(1)
    inputEmail = driver.find_element(By.ID, 'session_key')
    time.sleep(1)
    inputEmail.send_keys(email)
    time.sleep(1)
    inputKey = driver.find_element(By.ID,'session_password')
    time.sleep(1)
    inputKey.send_keys(senha)
    time.sleep(1)
    btnEntrar = driver.find_element(By.CSS_SELECTOR, '.btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width').click()
    print("Logando com sucesso!")
    time.sleep(60)

def iniciar():
    email = entry_email.get()
    senha = entry_senha.get()
    janela.destroy()
    logar(email, senha)
    time.sleep(60)

#-------------------------------------------------------------------------------------------------------

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")

label_email = tk.Label(janela, text="Email:")
label_email.pack(pady=10)
entry_email = tk.Entry(janela)
entry_email.pack(pady=10)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=10)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=10)

botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar)
botao_iniciar.pack(pady=20)

janela.mainloop()
