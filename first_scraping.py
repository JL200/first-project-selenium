'''
Selenium studies

author: João Luiz de Castro Pereira
'''
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ge.globo.com/")

menu_icon = driver.find_element(By.CSS_SELECTOR, '#header-produto > div.gui-color-primary-bg.header-principal.header-navegacao-color > div > div > div.menu-area > div > div')
menu_icon.click()

driver.find_element(By.CSS_SELECTOR, '#menu-1-brasileirao > a > span.menu-item-title').click()

table1 = driver.find_element(By.CSS_SELECTOR, '#classificacao__wrapper > article > section.tabela.tabela__pontos-corridos > div')
table2 = driver.find_element(By.CSS_SELECTOR, '#classificacao__wrapper > article > section.tabela.tabela__pontos-corridos > div > table.tabela__pontos')

df = pd.read_html(table1.get_attribute('outerHTML'))[0]
df.to_csv('tabel_brasileirao.csv', index=False)

df = pd.read_html(table2.get_attribute('outerHTML'))[0]
df.to_csv('data_brasileirao.csv', index=False)

driver.quit()

