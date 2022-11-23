# test.py

import pyautogui
import time
from pynput.keyboard import Key, Controller
import numpy

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
    pyautogui.moveTo(659, 1057) #Opens steam
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(219, 47) #Opens library
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(89, 287) #Opens bloons
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(371, 425) #Starts bloons
    pyautogui.click()
    time.sleep(7)
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
    pyautogui.click(x, y)
    pyautogui.press('backspace')
    
def startGame():
    keyB = Controller()
    keyB.press(Key.space)
    time.sleep(0.1)
    keyB.release(Key.space)
    keyB.press(Key.space)
    time.sleep(0.1)
    keyB.release(Key.space)

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

def findWidth(x, y):
    for i in range(66):
        n = x + i
        setDart(n, y)

def findHeight(x, y):
    for j in range(59):
        m = y + j
        setDart(x, m)

def findDiag(x, y):
    setDart(x, y)
    for i in range(39):
        n = x + i
        setDart(n, y - 46)
        
def createSquare(x, y):
    keyB = Controller()
    for i in range(2):
        for j in range(2):
            n = x + i*66
            m = y + j*59
            setDart(n, m)
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
                setDart(i, j) #Check initial
                pyautogui.moveTo(40, 20)
                time.sleep(0.1)
                pix = pyautogui.pixel(i, j)
                if pix[0] == 255 and pix[1] == 0 and pix[2] == 0:
                    NPlaceable[(i, j)] = 0
                else:
                    Placeable[(i, j)] = 0
                pyautogui.moveTo(1, 1)
    file1 = open("D:\School Stuff\Fall 2022\CS 4710 AI\BTD6 AI\MM.txt", "a")
    file1.write("SmallP: \n")
    for key, value in Placeable.items():
        file1.write('%s:%s\n' % (key, value))
    file1.write("SmallNP: \n")
    for key, value in NPlaceable.items():
        file1.write('%s:%s\n' % (key, value))
    file1.close()

def createMedGrid(): #For Boomerang, Bomb, Dartling, Wizard, Druid, Engineer, Heroes
    return 0

def createSubGrid(): #For Subs
    return 0

def createPirateGrid(): #For Pirates
    return 0

def createLargeGrid(): #For Spikes, Churchill, and Pat Fusty
    return 0

def createAceGrid(): #For Aces
    return 0

def createHeliGrid(): #For Helis
    return 0

def createFarmGrid(): #For Farms
    return 0

def findBlackPixH(x, y):
    r = 1/16
    for i in range(15):
        m = x + i
        if pyautogui.pixelMatchesColor(m, y, (0, 0, 0)):
            r *= 2
        if pyautogui.pixelMatchesColor(m, y + 1, (0, 0, 0)):
            r *= 3
    return r

def findBlackPixV(x, y):
    r = 1/12
    for i in range(33):
        n = y + i
        if pyautogui.pixelMatchesColor(x, n, (0, 0, 0)):
            r *= 2
        if pyautogui.pixelMatchesColor(x + 1, n, (0, 0, 0)):
            r *= 3
    return r

def findIntO(x, y):
    b = findBlackPixH(x, y)
    print(b)
    if b == 45:
        return 0
    elif b == 102036672:
        return 1
    elif b == 1296:
        return 2
    elif b == 54:
        return 3
    elif b == 1417176:
        return 4
    elif b == 20:
        return 5
    elif b == 186624:
        return 6
    elif b == 228509902503936:
        return 7
    elif b == 1889568:
        return 8
    elif b == 4251528:
        return 9
    else:
        return None

def findIntT(x, y):
    b = int(findBlackPixV(x, y))
    print(b)
    if b == 3690:
        return 0
    elif b == 102036672:
        return 1
    elif b == 559872:
        return 2
    elif b == 15552:
        return 3
    elif b == 6912:
        return 4
    elif b == 19042491875328:
        return 5
    elif b == 7558272:
        return 6
    elif b == 228509902503936:
        return 7
    elif b == 1889568:
        return 8
    elif b == 4251528:
        return 9
    else:
        return None
            
def findRound():
    hun = findIntO(1481, 33)
    ten = findIntT(1508, 33)
    one = findIntO(1541, 33)
    if hun == None:
        hun = 0
    if ten == None:
        ten = 0
    if one == None:
        one = 0
    r = (100 * hun) + (10 * ten) + (one)
    return r

print(pyautogui.size())
time.sleep(2)
print(pyautogui.position())
# startMMStandard()
# startMMSandbox()
# time.sleep(5)
# createSmallGrid()
# findBlackPix(1535, 33)
# x = findRound()
# print("Round: ")
# print(x)
t = pyautogui.locateAllOnScreen("D:\School Stuff\Fall 2022\CS 4710 AI\BTD6 AI\p1.png", confidence = 0.9)
for p in t:
    print(p)