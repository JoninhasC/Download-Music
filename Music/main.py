from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o ChromeDriver
chrome_driver_path = r'C:\Users\jonin\OneDrive\Documentos\GitHub\Download-Music\Music\chromedriver\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Abrir o arquivo com os links
with open(r'url\musica.txt', 'r') as file:
    urls = file.readlines()  # Lê todas as linhas (links) do arquivo

# Loop para cada URL do arquivo
for url in urls:
    url = url.strip()  # Remove espaços em branco ou quebras de linha

    if url:  # Certifica que não estamos processando uma linha vazia
        # Acessar o site
        driver.get("https://flvto.site/")
        time.sleep(2)

        # Localizar a caixa de pesquisa e inserir o link do YouTube
        search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Insert link to the media']")
        search_box.send_keys(url)  # Inserir o link da variável `url`
        time.sleep(2)

        # Clicar no botão de converter
        convert_button = driver.find_element(By.ID, "submit")
        convert_button.click()
        time.sleep(2)

        # Verificar se novas abas foram abertas
        all_tabs = driver.window_handles

        # Certificar-se de que há várias abas antes de tentar alternar
        if len(all_tabs) > 1:
            # Alternar para a nova aba
            driver.switch_to.window(all_tabs[1])

            # Fechar a nova aba
            driver.close()

            # Voltar para a aba original
            driver.switch_to.window(all_tabs[0])

        time.sleep(10)

        # Aguardar até que o botão esteja clicável
        try:
            download_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "mylink"))
            )

            # Scroll até o botão de download se necessário
            driver.execute_script("arguments[0].scrollIntoView();", download_button)

            # Clicar no botão de download
            download_button.click()
        except Exception as e:
            print(f"Erro ao clicar no botão de download: {e}")
            continue

        time.sleep(2)

        # Atualizar a lista de abas abertas
        all_tabs = driver.window_handles

        # Certificar-se de que há várias abas antes de tentar alternar novamente
        if len(all_tabs) > 1:
            # Alternar para a nova aba
            driver.switch_to.window(all_tabs[1])

            # Fechar a nova aba
            driver.close()

            # Voltar para a aba original
            driver.switch_to.window(all_tabs[0])

        time.sleep(7)

        # Localizar e clicar no botão final de download
        try:
            final_download_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "FLVTO"))
            )
            final_download_button.click()
        except Exception as e:
            print(f"Erro ao clicar no botão final de download: {e}")
            continue

        time.sleep(2)

# Fechar o navegador após o loop
driver.quit()


