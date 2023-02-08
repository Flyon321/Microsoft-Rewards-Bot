import pyautogui as pg
import time
import subprocess as sb
import random

# Funzioni di stampa colorata
global badprint
badprint = False # Impostare su True per disabilitare la stampa colorata
def rprint(skk): print(" E "+skk) if badprint else print("\033[91m E\033[00m {}" .format(skk))
def gprint(skk): print(" * "+skk) if badprint else print("\033[92m *\033[00m {}" .format(skk))
def xprint(skk): print(":: "+skk) if badprint else print(":: \033[96m{}\033[00m" .format(skk))

path_firefox = "C://Program Files//Mozilla Firefox//firefox.exe"
path_edge = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"

def new_window(program="Firefox"):
    if "Firefox" in program:
        sb.Popen(path_firefox)
    elif ("Edge" in program):
        sb.Popen(path_edge)
    else: # Mobile
        sb.Popen(path_firefox)
        change_device()
    gprint("Nuova finestra")
    time.sleep(1)

def close_window():
    with pg.hold('ctrl'):
        pg.press('w')
    gprint("Chiusa finestra")
    
def write():
    time.sleep(2)
    pg.typewrite(phrase, 0.03)
    time.sleep(2)
    pg.press('enter')
    print(">> "+phrase)
    time.sleep(2)

def change_device():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('m')
    time.sleep(1)
    gprint("Impostato dispositivo mobile")

def Generator():
    buono = ""
    caratteri = ["A","B","C","D","E","F","G","H","J","K","I","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "1","2","3","4","5","6","7","8","9","0"]
    for i in range(14):
        casuale = random.choice(caratteri)
        buono = buono + casuale
    return buono

# ---- MAIN ---
count_x = 0
count_y = 0
count_z = 0
x = int(input("Inserire il numero di ricerche da fare su Windows: "))
y = int(input("Inserire il numero di ricerche da fare su Mobile: "))
z = int(input("Inserire il numero di ricerche da fare su Edge: "))

# Point on Firefox
while count_x < x:
    new_window("Firefox")
    phrase = Generator()
    write()
    close_window()
    count_x = count_x + 1

# Point on Mobile
while count_y < y:
    new_window("Mobile")
    change_device()
    phrase = Generator()
    write()
    close_window()
    count_y = count_y + 1

while count_z < z:
    new_window("Edge")
    phrase = Generator()
    write()
    close_window()
    count_z = count_z + 1
