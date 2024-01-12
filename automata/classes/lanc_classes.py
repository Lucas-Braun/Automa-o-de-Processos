import pyautogui as nier
from time import sleep

with open('classes/testev4.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        extenso = linha.split(';')[0]
        descricao = linha.split(';')[1]
        # Clica no extenso
        nier.click(x=3375, y=436, duration=2) 
        nier.write(extenso)
        nier.click(x=3944, y=440, duration=2)
        nier.click(x=3879, y=464, duration=2)
        ########## 3 tab
        nier.click(x=3383, y=506, duration=2)
        nier.write(descricao)
        ######Credora
        nier.click(x=3944, y=505, duration=2)
        ### click devedora
        nier.click(x=3869, y=530, duration=2)
        ############ 4  tab -  x=3641, y=968
        nier.click(x=3824, y=969, duration=2)
        sleep(1)