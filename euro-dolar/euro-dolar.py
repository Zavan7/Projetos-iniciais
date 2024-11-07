from selenium import webdriver as opcao_selenium
from selenium.webdriver.common.keys import Keys
import pyautogui as pausaPc
import pyautogui as atalhosPc
from selenium.webdriver.common.by import By
import xlsxwriter
import os

abrirNavegador = opcao_selenium.Chrome()

meuNavegador = opcao_selenium.Chrome()
meuNavegador.get('https://www.google.com.br/?hl=pt-BR')

pausaPc.sleep(3)

meuNavegador.find_element(By.NAME, 'q').send_keys('Valor do dolar hoje')

pausaPc.sleep(1)

meuNavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
pausaPc.sleep(1)

valorDolar = meuNavegador.find_elements(By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > block-component > div > div.dG2XIf.XzTjhb > div > div > div > div > div.ifM9O > div > div > div > div > div.wDYxhc > div > span.ILfuVd > span > b')[0].text
pausaPc.sleep(1)

print('O valor do dolar é: ', valorDolar)

pausaPc.sleep(1)

meuNavegador.find_element(By.NAME, 'q').send_keys('')
pausaPc.sleep(1)

atalhosPc.press('tab')
pausaPc.sleep(1)
atalhosPc.press('enter')

meuNavegador.find_element(By.NAME, 'q').send_keys('Valor do euro hoje')
pausaPc.sleep(2)

meuNavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
valorEuro = meuNavegador.find_elements(By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > block-component > div > div.dG2XIf.XzTjhb > div > div > div > div > div.ifM9O > div > div > div > div > div:nth-child(2) > div > span > span > b')[0].text

print('O valor do euro é: ', valorEuro)

nomeCaminhoArquivo = 'C:\\Users\\Vtiro Zavan\\OneDrive\\Área de Trabalho\\python_rpa\\rpa_selenium\\Dolae e Euro.xlsx'
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()


sheet1.write('A1', 'Dolar')
sheet1.write('B1', 'Euro')
sheet1.write('A2', valorDolar)
sheet1.write('B2', valorEuro)

planilhaCriada.close()

os.startfile(nomeCaminhoArquivo)
