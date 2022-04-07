import pyautogui as pg
import time
import subprocess as sb

def close_tab():
    with pg.hold('ctrl'):
        pg.press('PgUp')
    time.sleep(0.5)
    with pg.hold('ctrl'):
        pg.press('w')

def write():
    time.sleep(2)
    pg.typewrite(phrase, 0.03)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)

def change_device():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('m')
    time.sleep(2)


count_x = 0
count_y = 0
x = int(input("Enter the number of searches to do on Windows: "))
y = int(input("Enter the number of searches to do on Mobile: "))

sb.Popen("C://Program Files//Mozilla Firefox//firefox.exe")

file_windows = open("site.txt")
phrase = file_windows.readline

time.sleep(6)
for phrase in file_windows:
    if count_x < x:
        write()

        with pg.hold('ctrl'):
            pg.press('t')

        time.sleep(0.5)
        close_tab()

        count_x = count_x + 1
    else:
        break

file_windows.close

file_mobile = open("site.txt")
phrase = file_mobile.readline

for phrase in file_mobile:
    if count_y < y:
        change_device()

        write()

        with pg.hold('ctrl'):
            pg.press('t')

        time.sleep(0.5)
        close_tab()

        count_y = count_y + 1
    else:
        break

file_mobile.close
