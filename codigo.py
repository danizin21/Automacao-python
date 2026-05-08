#pip install pyautogui
import pyautogui
import time
import pandas as pd

#pyautogui.click clica
#pyautogui.write escreve
#pyautogui.press aperta uma tecla
#pyautogui.hotkey aperta um atalho
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# passo 1: entrar no sistema da empresa
#abriria o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3) #pyautogui hashtag

#passo 2: fazer o login
#clicar no campo de email
pyautogui.click(x=528, y=394)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passa para o proximo campo
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

#passo 3: abrir a base de dados(importar o arquivo)
tabela = pd.read_csv("produtos.csv")



for linha in tabela.index:
    #passo 4: cadastrar 1 produto
    #codigo
    pyautogui.click(x=484, y=279)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) 
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    #voltar para o inicio da tela
    pyautogui.hotkey("ctrl", "home")   
    

#passo 5: repetir o passo 4 até acabar a lista de produtos

#nan = not a number