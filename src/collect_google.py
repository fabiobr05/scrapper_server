from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile

def iniciar_navegador():
    
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def buscar_google(data):
    descricao = "produto " + data["desc"]
    url = f"https://www.google.com/search?q={descricao}"

    driver = iniciar_navegador()
    try:
        driver.get(url)

        # Espera os títulos aparecerem
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
