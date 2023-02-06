import pyautogui as pg
import time
import subprocess as sb
import random

def new_window():
    time.sleep(3)
    with pg.hold('ctrl'):
        pg.press('n')
    time.sleep(2)

def close_window():
    with pg.hold('ctrl'):
        pg.press('w')

def write():
    time.sleep(3)
    pg.typewrite(phrase, 0.03)
    time.sleep(2)
    pg.press('enter')
    time.sleep(3)

def change_device():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('m')
    time.sleep(3)

def Generator():
    buono = ""
    caratteri = ["A","B","C","D","E","F","G","H","J","K","I","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "1","2","3","4","5","6","7","8","9","0"]
    for i in range(14):
        casuale = random.choice(caratteri)
        buono = buono + casuale

    return buono

count_x = 0
count_y = 0
count_z = 0
x = int(input("Inserire il numero di ricerche da fare su Windows: "))
y = int(input("Inserire il numero di ricerche da fare su Mobile: "))
z = int(input("Inserire il numero di ricerche da fare su Edge: "))

if x != 0 or y != 0:
    #Insert your Firefox path here
    sb.Popen("C://Program Files//Mozilla Firefox//firefox.exe")

    time.sleep(6)

    pg.write("ciao", 0.03)
    pg.press('enter')
    time.sleep(4)
    with pg.hold('ctrl'):
        pg.press('n')

    #Point on Browser

    while count_x < x:
        phrase = Generator()
        write()
        close_window()
        new_window()

        count_x = count_x + 1

    #Point on Mobile

    while count_y < y:
        change_device()

        phrase = Generator()
        write()
        close_window()
        new_window()

        count_y = count_y + 1

if z != 0:
    #Insert your Edge path here
    sb.Popen("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
    time.sleep(8)

    while count_z < z:
        phrase = Generator()
        write()
        close_window()
        new_window()

        count_z = count_z + 1
