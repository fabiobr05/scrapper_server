from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def buscar_duckduckgo(data):
    descricao = "produto " + data["desc"]
    url = f"https://html.duckduckgo.com/html/?q={descricao}&kl=br-pt"

    driver = iniciar_navegador()
    try:
        driver.get(url)

        # Espera as divs de resultados aparecerem (cada resultado em .result)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result__body"))
        )

        titulos = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
        descricoes = driver.find_elements(By.CSS_SELECTOR, "a.result__snippet")

        resultados = []
        for i in range(min(len(titulos), len(descricoes))):
            resultados.append({
                "titulo": titulos[i].text.strip(),
                "desc": descricoes[i].text.strip()
            })

        return resultados
    finally:
        driver.quit()
