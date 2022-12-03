import pyautogui
import time
from pynput.keyboard import Key, Controller
import numpy
import main

def findWidth(x, y):
    n = x
    main.setMonkey(10 ,(x, y))
    main.setMonkey(10, (x, y))
    pix = pyautogui.pixel(x, y+37)
    print(pix)
    while pix[0] == 255 and pix[1] == 0 and pix[2] == 0 and n-x < 200:
        n += 1
        main.setMonkey(10, (n, y))
        pix = pyautogui.pixel(n, y+37)
    main.sellTower((x, y))
    main.sellTower((n, y))
    return n-x

def findHeight(x, y):
    m = y
    main.setMonkey(10, (x, y))
    main.setMonkey(10, (x, y))
    pix = pyautogui.pixel(x, y+37)
    while pix[0] == 255 and pix[1] == 0 and pix[2] == 0 and m-y < 200:
        m += 1
        main.setMonkey(10, (x, m))
        pix = pyautogui.pixel(x, m+37)
    main.sellTower((x, y))
    main.sellTower((x, m))
    return m-y

def findDiag(x, y):
    main.setMonkey(1, (x, y))
    for i in range(39):
        n = x + i
        main.setMonkey(1, (n, y - 46))

def findRed(pos):
    for j in range(61):
        if pyautogui.pixel(pos[0], pos[1]-j)[0] == 255 and pyautogui.pixel(pos[0], pos[1]-j)[1] == 0 and pyautogui.pixel(pos[0], pos[1]-j)[2] == 0:
            return j
    return None
        
def createSquare(x, y):
    for i in range(2):
        for j in range(2):
            n = x + i*66
            m = y + j*59
            main.setMonkey(1, (n, m))
            pyautogui.moveTo(100, 100)
            time.sleep(0.1)
            pix = pyautogui.pixel(n, m)
            if pix[0] == 255 and pix[1] == 0 and pix[2] == 0:
                print("invalid")
            pyautogui.moveTo(1, 1)
    
def createSmallGrid(): #For Dart, Tack, Ice, Glue, Sniper, Ninja, Alch
    Placeable = {}
    NPlaceable = {}
    for i in range(66, 1980, 66):
        for j in range(59, 1080, 59):
            if (i < 1650 and j >= 118):
                main.setMonkey(1, (i,j)) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0: # Check if it's red
                    NPlaceable[(i, j)] = 0
                else: #If not red, it's placeable
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMSm.txt", "a")
    for key in Placeable.keys():
        file1.write(str(key) + "\n") 
    file1.write("\n")
    for key in NPlaceable.keys():
        file1.write(str(key) + "\n")
    file1.close()

def createMedGrid(): #For Boomerang, Bomb, Dartling, Wizard, Druid, Engineer, Heroes
    # x = findWidth(1000, 100)
    # y = findHeight(1000, 100)
    x = 77
    y = 67
    Placeable = {}
    NPlaceable = {}
    for i in range(x, 1980, x):
        for j in range(y, 1080, y):
            if (i < 1650 and j >= 118):
                main.setMonkey(2, (i, j)) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0: # Check if it's red
                    NPlaceable[(i, j)] = 0
                else: #If not red, it's placeable
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMMe.txt", "a")
    for key in Placeable.keys():
        file1.write(str(key) + "\n")
    file1.write("\n")
    for key in NPlaceable.keys():
        file1.write(str(key) + "\n")
    file1.close()

def createSubGrid(): #For Subs
    return 0

def createPirateGrid(): #For Pirates
    return 0

def createLargeGrid(): #For Spikes, Churchill, and Pat Fusty
    x = 87
    y = 75
    Placeable = {}
    NPlaceable = {}
    for i in range(x, 1980, x):
        for j in range(y, 1080, y):
            if (i < 1650 and j >= 118):
                main.setMonkey(20, (i, j)) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j-60)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0: # Check if it's red
                    NPlaceable[(i, j)] = 0
                else: #If not red, it's placeable
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open(r"C:\Users\Max\Documents\GitHub\BTD6-AI\MMLa.txt", "a")
    for key in Placeable.keys():
        file1.write(str(key) + "\n")
    file1.write("\n")
    for key in NPlaceable.keys():
        file1.write(str(key) + "\n")
    file1.close()

def createAceGrid(): #For Aces
    x = 152
    y = 85
    Placeable = {}
    NPlaceable = {}
    for i in range(x, 1980, x):
        for j in range(y, 1080, y):
            if (i < 1650 and j >= 118):
                main.setMonkey(10, (i, j)) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j+37)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0: # Check if it's red
                    NPlaceable[(i, j)] = 0
                else: #If not red, it's placeable
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMAc.txt", "a")
    for key in Placeable.keys():
        file1.write(str(key) + "\n")
    file1.write("\n")
    for key in NPlaceable.keys():
        file1.write(str(key) + "\n")
    file1.close()

def createHeliGrid(): #For Helis
    x = 146
    y = 127
    Placeable = {}
    NPlaceable = {}
    for i in range(x, 1980, x):
        for j in range(y, 1080, y):
            if (i < 1650 and j >= 118):
                main.setMonkey(11, (i, j)) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j+58)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0: # Check if it's red
                    NPlaceable[(i, j)] = 0
                else: #If not red, it's placeable
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMHe.txt", "a")
    for key in Placeable.keys():
        file1.write(str(key) + "\n")
    file1.write("\n")
    for key in NPlaceable.keys():
        file1.write(str(key) + "\n")
    file1.close()

def createFarmGrid(): #For Farms
    return 0