# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://servicos.sjc.sp.gov.br/portal_da_transparencia/despesa_funcao.aspx")

select = driver.find_element(By.NAME, "ctl00$cphConteudo$cmbPeriodo")

select.select_by_value('202305')