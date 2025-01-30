import pandas as pd
import pyautogui         # para manipular acoes teclado e mouse
import time

#Iniciando a automação
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)  
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link 
time.sleep(1)
pyautogui.write('https://sauer.pro.br/python/automacao/index.html')
pyautogui.press('enter')

# Passo 2: Fazer login
# selecionar o campo de login
time.sleep(1)
pyautogui.click(x=633, y=518)   # ou - pyautogui.press('tab')

# escrever o usuário na posição capturada
pyautogui.write('admin')              # login
pyautogui.press('tab')
pyautogui.write('simplificapython')   # senha
pyautogui.press('tab')
pyautogui.press('enter')

tabela = pd.read_csv('alunos.csv')    # panda manipular excel
time.sleep(3)

for linha in tabela.index:
  pyautogui.click(x=727, y=331)   # posição na tela

  nome = tabela.loc[linha, 'Nome']    # loc é para localizar
  pyautogui.write(nome)
  pyautogui.press('tab')

  email = tabela.loc[linha, 'Email'] 
  pyautogui.write(email) 
  pyautogui.press('tab')

  endereco = tabela.loc[linha, 'Endereco']
  pyautogui.write(endereco)
  pyautogui.press('tab')

  telefone = tabela.loc[linha, 'Telefone']
  pyautogui.write(telefone)
  pyautogui.press('tab')

  pyautogui.press('enter')
  time.sleep(3)
  pyautogui.scroll(5000)


# exemplo
# tabela = pd.read_csv('alunos.csv')   # pandas
# print(tabela.loc[1, 'Nome'])