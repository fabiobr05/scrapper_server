import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def iniciar_navegador():
    options = uc.ChromeOptions()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    
    # Forçar o uso do chromedriver do sistema
    # uc normalmente baixa e gerencia seu próprio driver, 
    # mas podemos forçar o uso do driver externo definindo o parâmetro driver_executable_path
    driver = uc.Chrome(options=options, driver_executable_path='/usr/bin/chromedriver')
    return driver

descricao = "produto coca cola lata"
driver = iniciar_navegador()

try:
    driver.get(f'https://www.google.com/search?q={descricao}')
    sleep(3)

    sleep(5)  # dar um tempinho para carregar
    print(driver.page_source)  # imprime o HTML carregado

    titulos = driver.find_elements(By.CLASS_NAME, "LC20lb")
    descricoes = driver.find_elements(By.CLASS_NAME, "VwiC3b")

    resultados = []
    for i in range(min(len(titulos), len(descricoes))):
        resultados.append({
            "titulo": titulos[i].text.strip(),
            "desc": descricoes[i].text.strip()
        })

    print(resultados)
finally:
    driver.quit()
