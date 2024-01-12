
import pyautogui
import pandas as pd    
import time 

pyautogui.PAUSE = 0.3

##tabela = pd.read_csv("create_classes.csv")

tabela = pd.read_csv("create_classes.csv", delimiter=';')
        
print(tabela)

for linha in tabela.index:
    ## Clicar no campo valor
    pyautogui.click(x=4496, y=73)
    ##########3
    pyautogui.click(x=3344, y=436)
        # pegar da tabela o valor do campo que a gente quer preencher
    ##codigo = tabela.loc[linha, "Extenso"] 
    ########################
    codigo = tabela.loc[linha, "Reduzido"]
    # preencher o campo
    pyautogui.write(str(codigo))
    ########################
    ## Escreve o cod. extenso
    pyautogui.write(str(tabela.loc[linha, "Extenso"]))
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.write(str(tabela.loc[linha, "Descrição"]))
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')




