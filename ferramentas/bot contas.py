from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

# Função para gerar um nome de usuário aleatório
def generate_username(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Função para gerar uma senha aleatória
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Número de contas que você deseja criar
num_accounts = 10

# Inicializa o navegador
chrome_driver_path = "C:/Users/mocob/Desktop/PASTAS/chromedriver_win32.exe"  # Caminho para o ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Lista para armazenar os detalhes das contas
account_details = []

for _ in range(num_accounts):
    # Gera um nome de usuário e senha aleatórios
    username = generate_username()
    password = generate_password()

    # Abre a página de registro do Instagram
    driver.get("https://www.instagram.com/accounts/emailsignup/")

    # Preenche o nome de usuário e a senha
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    # Clica no botão de registro
    driver.find_element_by_css_selector("button[type='submit']").click()

    # Aguarda um tempo para garantir que a página seja carregada completamente
    driver.implicitly_wait(5)

    # Armazena os detalhes da conta
    account_details.append({"username": username, "password": password})

# Fecha o navegador
driver.quit()

# Salva os detalhes das contas em um arquivo txt
with open("contas_instagram.txt", "w") as file:
    for account in account_details:
        file.write(f"Username: {account['username']}, Password: {account['password']}\n")
