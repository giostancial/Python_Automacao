# Passo 1 -  Entrar no sistema
# Passo 2 - Fazer login
# Passo 3 - Pegar/Impotar base de dados
# Passo 4 - Cadastrar produto
# Passo 5 - Repetir até acabar a lista de produtos

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclas (ex: ctrl + c)
# pyautogui.scroll - rolar a tela
# pyautogui.PAUSE - configuração para cada comando vai dar uma pausa de x tempo
# time.sleep - fará uma pausa no local usado

pyautogui.PAUSE = 1
# Passo 1 
# Abrir navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2
# Fazer login
pyautogui.click(x=887, y=448)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("exemplo@gmail.com")

pyautogui.press("tab")
pyautogui.write("123")

pyautogui.click(x=984, y=647)

time.sleep(3)

# Passo 3
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4

for linha in tabela.index:

    # código
    pyautogui.click(x=918, y=310)
    codigo = str(tabela.loc[linha, "codigo"])  # str transforam em string
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    # tipo 
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # categoria 
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    # custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":    # != é diferente(>=)
        pyautogui.write(obs)

    # enter

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

# Passo 5
