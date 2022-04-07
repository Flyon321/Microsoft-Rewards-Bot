import pyautogui as pg
import time
import subprocess as sb

def new_tab():
    with pg.hold('ctrl'):
        pg.press('t')
    time.sleep(0.5)

def close_window():
    with pg.hold('ctrl'):
        pg.press('w')

def close_tab():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('tab')
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
count_z = 0
x = int(input("Enter the number of searches to do on Windows: "))
y = int(input("Enter the number of searches to do on Mobile: "))
z = int(input("Enter the number of searches to do on Edge: "))

if x != 0 or y != 0:
    #Earn on Firefox Windows
    sb.Popen("C://Program Files//Mozilla Firefox//firefox.exe")
    
    file_windows = open("site.txt")
    phrase = file_windows.readline

    time.sleep(6)

    for phrase in file_windows:
        if count_x < x:
            write()
            new_tab()
            close_tab()

            count_x = count_x + 1
        else:
            break

    file_windows.close

    #Punti su Mobile
    file_mobile = open("site.txt")
    phrase = file_mobile.readline

    for phrase in file_mobile:
        if count_y < y:
            change_device()

            write()
            new_tab()
            close_tab()

            count_y = count_y + 1
        else:
            break

    close_window()
    file_mobile.close

#Punti su Edge
if z != 0:
    sb.Popen("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
    time.sleep(8)

    file_edge = open("site.txt")
    phrase = file_edge.readline

    time.sleep(6)
    for phrase in file_edge:
        if count_z < z:
            write()
            new_tab()
            close_tab()

            count_z = count_z + 1
        else:
            break

    close_window()
    file_edge.close
