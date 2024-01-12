import pyautogui as nier
from time import sleep

with open('irineu.txt', 'r', encoding='utf-8') as arquivo:
    next(arquivo)  # Pula a primeira linha (cabeçalho)
    for linha in arquivo:
        reduzido = linha.split()[0]
        print("Escrevendo:", reduzido)  # Adicionado para depuração
        ##Clicar no campo de pesquisa
        nier.click(x=2858, y=85, duration=2)
        nier.click(x=2858, y=85, duration=1)
        sleep(0.5)  # Pequeno atraso para garantir que a interface responda
        ## escrever
        nier.write(reduzido)
        sleep(0.5)  # Pequeno atraso após escrever
        ## cLICAR NA LUPA
        nier.click(x=2943, y=78, duration=2)
        nier.click(x=2943, y=78, duration=1)
        ######## clica no resultado da pesquisa
        nier.click(x=3284, y=176, duration=2)
        #### Clica para excluir 
        nier.click(x=4653, y=80, duration=2)
        ##### Confirmar a exclusão 
        nier.click(x=3588, y=718, duration=2)
        sleep(1)
