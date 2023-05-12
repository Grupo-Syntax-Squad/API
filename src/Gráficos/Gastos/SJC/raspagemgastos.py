# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
anos = ['2022']

for ano in anos:
    pasta = f"C:/Users/Wellington/Documents/GitHub/API/src/Gráficos/Gastos/SJC/Gastos{ano}"

    # Vê se a pasta do respectivo ano existe
    if not os.path.exists(pasta):
        # Se não existir cria
        os.makedirs(pasta)

    for mes in meses:
        data = f"{mes}/{ano}"
        # Abrindo o portal de transparência
        driver.get("https://servicos.sjc.sp.gov.br/portal_da_transparencia/despesa_funcao.aspx")

        # Encontrando o menu dropdown
        select = driver.find_element(By.NAME, "ctl00$cphConteudo$cmbPeriodo")

        # Clicando no menu
        select.click()

        try:
            # Encontrando e clicando no mês desejado.
            driver.find_element(By.XPATH, f"//option[.='{data}']").click()

            # Encontrando e clicando no link para exportar os dados.
            driver.find_element(By.ID, 'ctl00_cphConteudo_lnkExportarLista').click()
            time.sleep(1)
        except:
            pass
    
    for c in range(12):
        if c == 0:
            os.replace('C:/Users/Wellington/Downloads/despesa_funcao.csv', f'C:/Users/Wellington/Documents/GitHub/API/src/Gráficos/Gastos/SJC/Gastos{ano}/despesa_funcao.csv')
        else:
            os.replace(f'C:/Users/Wellington/Downloads/despesa_funcao ({c}).csv', f'C:/Users/Wellington/Documents/GitHub/API/src/Gráficos/Gastos/SJC/Gastos{ano}/despesa_funcao ({c}).csv')
