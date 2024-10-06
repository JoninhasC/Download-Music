from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o arquivo de URLs
arquivo_txt = ''

# Configurando o driver (você precisa ter o driver do navegador que estiver usando, como o chromedriver)
driver = webdriver.Chrome(executable_path='caminho_para_chromedriver')


# Função para processar cada URL
def processar_url(url):
    driver.get('https://o-seu-site.com')  # substitua com o URL do site que você quer acessar

    # Espera o campo de inserção de link estar visível
    campo_url = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_do_campo_url'))  # ajuste para o ID correto do campo
    )

    # Insere o link no campo
    campo_url.send_keys(url)

    # Clica no botão para iniciar
    botao_iniciar = driver.find_element(By.ID, 'id_do_botao_iniciar')  # ajuste o ID conforme necessário
    botao_iniciar.click()

    # Aguarda o carregamento da barra
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'classe_da_barra_carregamento_completa'))
        # ajuste conforme o seletor da barra de progresso
    )

    # Clica no botão verde após carregar
    botao_verde = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'classe_do_botao_verde'))  # ajuste o seletor do botão verde
    )
    botao_verde.click()

    # Espera e clica no botão de fechar
    botao_fechar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'classe_do_botao_fechar'))  # ajuste conforme necessário
    )
    botao_fechar.click()


# Ler o arquivo de URLs
with open(arquivo_txt, 'r') as arquivo:
    urls = arquivo.readlines()

# Processar cada URL
for url in urls:
    processar_url(url.strip())

# Fechar o navegador ao fim
driver.quit()
