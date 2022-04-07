import pyautogui as pg
import time
import subprocess as sb

def chiudi_scheda():
    with pg.hold('ctrl'):
        pg.press('PgUp')
    time.sleep(0.5)
    with pg.hold('ctrl'):
        pg.press('w')

def scrivi():
    time.sleep(2)
    pg.typewrite(phrase, 0.03)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)

def cambio_dispositivo():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('m')
    time.sleep(2)

#time.sleep(4)

count_x = 0
count_y = 0
x = int(input("Inserire il numero di ricerche da fare su Windows: "))
y = int(input("Inserire il numero di ricerche da fare su Mobile: "))

sb.Popen("C://Program Files//Mozilla Firefox//firefox.exe")

file_windows = open("C://Users//Lenovo//Desktop//PROGRAMMING//cose_da_scrivere.txt")
phrase = file_windows.readline

time.sleep(6)
for phrase in file_windows:
    if count_x < x:
        scrivi()

        with pg.hold('ctrl'):
            pg.press('t')

        time.sleep(0.5)
        chiudi_scheda()

        count_x = count_x + 1
    else:
        break

file_windows.close

file_mobile = open("C://Users//Lenovo//Desktop//PROGRAMMING//cose_da_scrivere.txt")
phrase = file_mobile.readline

for phrase in file_mobile:
    if count_y < y:
        cambio_dispositivo()

        scrivi()

        with pg.hold('ctrl'):
            pg.press('t')

        time.sleep(0.5)
        chiudi_scheda()

        count_y = count_y + 1
    else:
        break

file_mobile.close