# test.py

import pyautogui
import time
from pynput.keyboard import Key, Controller
import numpy
import operator
import subprocess

def clickMonkeyMeadow():
    pyautogui.moveTo(534, 230) #Clicks "Monkey Meadow"
    pyautogui.click()
    time.sleep(0.3)

def clickEasy():
    pyautogui.moveTo(615, 401) #Clicks "Easy"
    pyautogui.click()
    time.sleep(0.3)

def clickStandard():
    pyautogui.moveTo(623, 573) #Clicks "Standard"
    pyautogui.click()
    time.sleep(0.3)

def clickSandbox():
    pyautogui.moveTo(954, 720) #Clicks "Sandbox"
    pyautogui.click()
    time.sleep(0.3)

def startBloons():
    # subprocess.call(r"D:\Steam\steam.exe -applaunch 960090") # Path for Desktop
    # time.sleep(7) # Sleep for Desktop
    subprocess.call(r"D:\Steam\steam.exe -applaunch 960090") # Path for laptop
    time.sleep(9) # Sleep for laptop
    pyautogui.moveTo(941, 985) #Clicks the start button and gets through the intro
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(827, 924) #Clicks "Play"
    pyautogui.click()
    time.sleep(0.3)
    
def setHero(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('u')
    keyB.release('u')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setDart(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('q')
    keyB.release('q')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setBoomerang(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('w')
    keyB.release('w')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setBomb(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('e')
    keyB.release('e')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setTack(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('r')
    keyB.release('r')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setIce(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('t')
    keyB.release('t')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setGlue(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('y')
    keyB.release('y')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setSniper(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('z')
    keyB.release('z')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setSub(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('x')
    keyB.release('x')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setPirate(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('c')
    keyB.release('c')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setAce(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('v')
    keyB.release('v')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setHeli(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('b')
    keyB.release('b')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setMortar(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('n')
    keyB.release('n')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setDartling(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('m')
    keyB.release('m')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setWizard(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('a')
    keyB.release('a')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setSuper(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('s')
    keyB.release('s')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setNinja(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('d')
    keyB.release('d')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setAlch(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('f')
    keyB.release('f')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setDruid(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('g')
    keyB.release('g')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setFarm(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('h')
    keyB.release('h')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setSpike(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('j')
    keyB.release('j')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setVillage(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('k')
    keyB.release('k')
    time.sleep(0.1)
    pyautogui.click(x, y)

def setEngineer(x, y):
    keyB = Controller()
    pyautogui.moveTo(x, y)
    keyB.press('l')
    keyB.release('l')
    time.sleep(0.1)
    pyautogui.click(x, y)

def upgrade1(x, y):
    keyB = Controller()
    pyautogui.click(x, y)
    keyB.press(',')
    time.sleep(0.1)
    keyB.release(',')
    keyB.press(Key.esc)
    keyB.release(Key.esc)

def upgrade2(x, y):
    keyB = Controller()
    pyautogui.click(x, y)
    keyB.press('.')
    time.sleep(0.1)
    keyB.release('.')
    keyB.press(Key.esc)
    keyB.release(Key.esc)

def upgrade3(x, y):
    keyB = Controller()
    pyautogui.click(x, y)
    keyB.press('/')
    time.sleep(0.1)
    keyB.release('/')
    keyB.press(Key.esc)
    keyB.release(Key.esc)

def sellTower(x, y):
    keyB = Controller()
    pyautogui.click(x, y)
    keyB.press(Key.backspace)
    time.sleep(0.1)
    keyB.release(Key.backspace)
    
def startGame():
    keyB = Controller()
    keyB.press(Key.space)
    time.sleep(0.1)
    keyB.release(Key.space)
    keyB.press(Key.space)
    time.sleep(0.1)
    keyB.release(Key.space)

def nextRound():
    keyB = Controller()
    keyB.press(Key.space)
    time.sleep(0.1)
    keyB.release(Key.space)

def isStopped():
    return len(list(pyautogui.locateAllOnScreen(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\start.png"))) != 0

def startMMStandard():
    startBloons()
    clickMonkeyMeadow()
    clickEasy()
    clickStandard()

def startMMSandbox():
    startBloons()
    clickMonkeyMeadow()
    clickEasy()
    clickSandbox()

def findNums(): # Maybe alter to take in a screen and then use it per location?
    ret = [0, 0, 0]
    lives = {}
    cash = {}
    roun = {}
    gen = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8 : {}, 9: {}}
    screen = pyautogui.screenshot(region=(0, 0, 1650, 150))
    zer = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p0.png", screen, confidence = 0.8)
    one = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p1.png", screen, confidence = 0.85)
    two = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p2.png", screen, confidence = 0.8)
    thr = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p3.png", screen, confidence = 0.8)
    fou = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p4.png", screen, confidence = 0.8)
    fiv = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p5.png", screen, confidence = 0.8)
    six = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p6.png", screen, confidence = 0.8)
    sev = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p7.png", screen, confidence = 0.8)
    eig = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p8.png", screen, confidence = 0.8)
    nin = pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\p9.png", screen, confidence = 0.8)
    for a in zer:
        t = True
        for z in gen[0].keys():
            if a[0] < z + 5 and a[0] > z - 5:
                t = False
        if t:
            gen[0][a[0]] = 1
    for b in one:
        t = True
        for o in gen[1].keys():
            if b[0] < o + 5 and b[0] > o - 5:
                t = False
        if t:
            gen[1][b[0]] = 1
    for c in two:
        t = True
        for tw in gen[2].keys():
            if c[0] < tw + 5 and c[0] > tw - 5:
                t = False
        if t:
            gen[2][c[0]] = 1
    for d in thr:
        t = True
        for th in gen[3].keys():
            if d[0] < th + 5 and d[0] > th - 5:
                t = False
        if t:
            gen[3][d[0]] = 1
    for e in fou:
        t = True
        for fo in gen[4].keys():
            if e[0] < fo + 5 and e[0] > fo - 5:
                t = False
        if t:
            gen[4][e[0]] = 1
    for f in fiv:
        t = True
        for fi in gen[5].keys():
            if f[0] < fi + 5 and f[0] > fi - 5:
                t = False
        if t:
            gen[5][f[0]] = 1
    for g in six:
        t = True
        for si in gen[6].keys():
            if g[0] < si + 5 and g[0] > si - 5:
                t = False
        if t:
            gen[6][g[0]] = 1
    for h in sev:
        t = True
        for se in gen[7].keys():
            if h[0] < se + 5 and h[0] > se - 5:
                t = False
        if t:
            gen[7][h[0]] = 1
    for i in eig:
        t = True
        for ei in gen[8].keys():
            if i[0] < ei + 5 and i[0] > ei - 5:
                t = False
        if t:
            gen[8][i[0]] = 1
    for j in nin:
        t = True
        for ni in gen[9].keys():
            if j[0] < ni + 5 and j[0] > ni - 5:
                t = False
        if t:
            gen[9][j[0]] = 1
    for it in gen.keys():
        if len(gen[it]) != 0:
            for ite in gen[it].keys():
                if ite < 275:
                    lives[ite] = it
                if ite < 700 and ite > 275:
                    cash[ite] = it
                if ite > 1000 and ite < 1500:
                    roun[ite] = it
    livesS = sorted(lives.items(), key=operator.itemgetter(0), reverse=True)
    cashS = sorted(cash.items(), key=operator.itemgetter(0), reverse=True)
    rounS = sorted(roun.items(), key=operator.itemgetter(0), reverse=True)
    k = 0
    for liv in livesS:
        ret[0] += liv[1] * (10 ** k)
        k+=1
    l = 0
    for cas in cashS:
        ret[1] += cas[1] * (10 ** l)
        l+=1
    m = 0
    for rou in rounS:
        ret[2] += rou[1] * (10 ** m)
        m+=1
    return ret # returned as lives, cash, and round

print(pyautogui.size())
time.sleep(2)
print(pyautogui.position())
# startMMStandard()
# startMMSandbox()
# time.sleep(5)
# createSmallGrid()
# print(findNums())
# print(findWidth(1000, 100))
# print(findHeight(1000, 100))
