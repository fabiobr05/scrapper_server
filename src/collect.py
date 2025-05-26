from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

import os
import tempfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def iniciar_navegador():
    options = Options()
    
    # Caminho para o Chromium
    options.binary_location = "/usr/bin/chromium"  # Caminho do Chromium no contêiner
    options.add_argument('--headless')  # Modo headless (remover se você não quiser headless)
    options.add_argument('--no-sandbox')  # Necessário para rodar no Docker
    options.add_argument('--disable-gpu')  # Desativa a GPU (sem suporte headless)
    options.add_argument('--disable-dev-shm-usage')  # Necessário para containers Docker
    
    # Cria um diretório temporário para dados de usuário
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')

    # Caminho para o chromedriver
    chromedriver_path = "/usr/bin/chromedriver"  # Caminho absoluto para o chromedriver

    # Usando a classe Service para passar o caminho do chromedriver
    service = Service(executable_path=chromedriver_path)

    # Inicializando o WebDriver com a classe Service
    driver = webdriver.Chrome(service=service, options=options)

    return driver


def buscar_google(data):
    descricao = "produto " + data["desc"]
    url = f"https://www.google.com/search?q={descricao}"

    driver = iniciar_navegador()
    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "LC20lb"))
        )

        titulos = driver.find_elements(By.CLASS_NAME, "LC20lb")
        descricoes = driver.find_elements(By.CLASS_NAME, "VwiC3b")

        resultados = []
        for i in range(min(len(titulos), len(descricoes))):
            resultados.append({
                "titulo": titulos[i].text.strip(),
                "desc": descricoes[i].text.strip()
            })

        return resultados
    finally:
        driver.quit()
