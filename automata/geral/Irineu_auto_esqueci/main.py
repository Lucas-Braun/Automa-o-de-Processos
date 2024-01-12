
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.3

tabela = pd.read_csv("cadastro_contabil.csv")

print(tabela)

for linha in tabela.index:
    ## Clicar no campo valor
    pyautogui.click(x=2796, y=79)
        # pegar da tabela o valor do campo que a gente quer preencher
    ##codigo = tabela.loc[linha, "Extenso"]
    ########################
    codigo = tabela.loc[linha, "Reduzido"]
    # preencher o campo
    pyautogui.write(str(codigo))
    ########################
    ## Escreve o cod. extenso
    pyautogui.write(str(tabela.loc[linha, "Extenso"]))
        # preencher o campo
    pyautogui.write(str(codigo))
    # Clicar na Lupa #
    pyautogui.click(x=2943, y=80)
    #Clica no resultado 
    pyautogui.click(x=3170, y=185)
    # Clicar para editar
    pyautogui.click(x=4571, y=83)
    # Clicar em CONTAS Comtabeis
    pyautogui.click(x=3356, y=400)
    #Clica NO RESULTADO
    pyautogui.click(x=3480, y=459)
    ## cLICA EM INSERIR
    pyautogui.click(x=3930, y=438)
    ## Clica em conta comtabil
    pyautogui.click(x=3416, y=601)
    ## pega o valor do csv
    pyautogui.write(str(tabela.loc[linha, "Conta_Reduzida"]))
    ## dat Tab par proximo campo
    pyautogui.press("tab")
    ## Tipod e Documento CLA1 escreve
    pyautogui.write("CLA1")
    ## TAB
    pyautogui.press("tab")
    ## clica Comfirmar 
    pyautogui.click(x=3848, y=755)