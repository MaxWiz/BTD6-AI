# test.py

from turtle import pos, position
import pyautogui
import time
from pynput.keyboard import Key, Controller
import numpy
import operator
import subprocess
import grid

##################################### UI COMMANDS #####################################

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

##################################### SETTER COMMANDS #####################################

def getMonkeyButton(index):
    if index == 0: # Hero
        return "u"
    if index == 1: # Dart
        return "q"
    if index == 2: # Boomerang
        return "w"
    if index == 3: # Bomb
        return "e"
    if index == 4: # Tack
        return "r"
    if index == 5: # Ice
        return "t"
    if index == 6: # Glue
        return "y"
    if index == 7: # Sniper
        return "z"
    if index == 8: # Sub
        return "x"
    if index == 9: # Pirate
        return "c"
    if index == 10: # Ace
        return "v"
    if index == 11: # Heli
        return "b"
    if index == 12: # Mortar
        return "n"
    if index == 13: # Dartling
        return "m"
    if index == 14: # Wizard
        return "a"
    if index == 15: # Super
        return "s"
    if index == 16: # Ninja
        return "d"
    if index == 17: # Alch
        return "f"
    if index == 18: # Druid
        return "g"
    if index == 19: # Farm
        return "h"
    if index == 20: # Spike
        return "j"
    if index == 21: # Village
        return "k"
    if index == 22: # Engi
        return "l"
    
def setMonkey(index, point):
    keyB = Controller()
    pyautogui.moveTo(point[0], point[1])
    key = getMonkeyButton(index)
    keyB.press(key)
    keyB.release(key)
    time.sleep(0.1)
    pyautogui.click(point[0], point[1])

def getUpgradeButton(index):
    if index == 1:
        return ","
    if index == 2:
        return "."
    if index == 3:
        return "/"

def upgrade(index, point):
    keyB = Controller()
    pyautogui.click(point[0], point[1])
    key = getUpgradeButton(index)
    keyB.press(key)
    time.sleep(0.1)
    keyB.release(key)
    keyB.press(Key.esc)
    keyB.release(Key.esc)

def sellTower(point):
    keyB = Controller()
    pyautogui.click(point[0], point[1])
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

##################################### SCREEN READING COMMANDS #####################################

def isStopped():
    screen = pyautogui.screenshot(region=(1650, 950, 330, 130))
    return len(list(pyautogui.locateAll(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\start.png", screen))) != 0

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

##################################### PRICE COMMANDS #####################################

def priceListEasy():
    #MADE FOR USE WITH QUINCY
    #Order is hero, dart, boom, bomb, tack, ice, glue, sniper, sub, pirate, ace, heli, mortar, dartling, wizard, super, ninja, alch, druid, farm, spike, town, engi
    r = [460, 170, 275, 445, 240, 425, 235, 300, 275, 425, 680, 1360, 640, 720, 320, 2125, 425, 470, 340, 1060, 850, 1020, 340]
    return r

def upgradeListEasy():
    r = [
        [ # Hero
            [1000000, 1000000, 1000000, 1000000, 1000000], # Dummy values to make PUindex consistient
            [1000000, 1000000, 1000000, 1000000, 1000000],
            [1000000, 1000000, 1000000, 1000000, 1000000]
        ],
        [ # Dart Monkey
            [120, 185, 255, 1530, 12750],
            [85, 160, 340, 6800, 38250],
            [75, 170, 530, 1700, 19975]
        ],
        [ # Boomerang
            [170, 240, 1105, 2550, 27540],
            [150, 210, 1230, 3570, 29750],
            [85, 255, 1105, 1870, 42500]
        ],
        [ # Bomb
            [295, 550, 1020, 3060, 46750],
            [210, 340, 930, 2720, 21250],
            [170, 255, 680, 2380, 29750]
        ],
        [ # Tack
            [125, 255, 510, 2975, 38675],
            [85, 190, 465, 2295, 12750],
            [85, 85, 380, 2720, 17000]
        ],
        [ # Ice
            [85, 295, 1275, 1870, 23800],
            [190, 295, 2465, 2550, 17000],
            [150, 190, 1655, 2335, 25500]
        ],
        [ # Glue
            [170, 255, 2125, 4250, 18700],
            [85, 1530, 2760, 2975, 12750],
            [100, 340, 2890, 2550, 23800]
        ],
        [ # Sniper
            [295, 1275, 2550, 4250, 28900],
            [255, 380, 2720, 6120, 11050],
            [340, 340, 2975, 3610, 11900]
        ],
        [ # Sub
            [110, 425, 425, 2125, 27200],
            [380, 255, 1190, 11050, 27200],
            [380, 850, 935, 2550, 21250]
        ],
        [ # Pirate
            [295, 465, 2505, 6120, 7200, 21250],
            [465, 425, 765, 3823, 17850],
            [155, 340, 1955, 4675, 19550]
        ],
        [ # Ace
            [550, 550, 850, 2550, 34000],
            [170, 295, 765, 15300, 25500],
            [425, 255, 1870, 20400, 72250]
        ],
        [ # Heli
            [680, 425, 1485, 16660, 38250],
            [255, 510, 2550, 10200, 25500],
            [210, 295, 2975, 7225, 29750]
        ],
        [ # Mortar
            [425, 425, 765, 6800, 23800],
            [255, 425, 765, 4675, 25500],
            [170, 425, 595, 9350, 34000]
        ],
        [ # Dartling
            [255, 765, 3610, 9350, 68000],
            [210, 805, 4460, 4335, 51000],
            [125, 1020, 2890, 10200, 49300]
        ],
        [ # Wizard
            [125, 510, 1105, 8500, 27200],
            [255, 805, 2550, 3400, 45900],
            [255, 255, 1445, 2380, 20400]
        ],
        [ # Super
            [2125, 2550, 17000, 85000, 425000],
            [850, 1190, 6800, 16150, 76500],
            [2550, 1020, 4760, 51000, 170000]
        ],
        [ # Ninja
            [255, 295, 720, 2335, 29750],
            [295, 425, 765, 4420, 18700],
            [210, 340, 2335, 3825, 34000]
        ],
        [ # Alch
            [210, 295, 1060, 2550, 51000],
            [210, 405, 2550, 3825, 38250],
            [550, 380, 850, 2335, 34000]
        ],
        [ # Druid
            [210, 850, 1400, 3825, 55250],
            [210, 295, 805, 4250, 29750],
            [85, 255, 510, 2125, 38250]
        ],
        [ # Farm
            [425, 510, 2550, 16150, 85000],
            [255, 680, 2975, 6375, 85000],
            [210, 170, 2465, 12750, 51000]
        ],
        [ # Spike
            [680, 510, 1955, 8075, 127500],
            [510, 680, 2125, 4250, 34000],
            [125, 340, 1190, 2975, 25500]
        ],
        [ # Village
            [340, 1275, 680, 2125, 21250],
            [210, 1700, 6375, 17000, 34000],
            [425, 425, 8500, 2550, 4250]
        ],
        [ # Engi
            [425, 340, 490, 2125, 27200],
            [210, 295, 680, 11475, 102000],
            [380, 185, 425, 2975, 45900]
        ]
    ]
    return r

##################################### CLASSES #####################################

class Monkey:
    
    def __init__(self, position, index):
        self.upgrades = [0, 0, 0]
        self.name = "" # Maybe unneeded?
        self.position = position
        self.PUindex = index

class Player:

    def __init__(self, priceList, upgradeList):
        # self.monkeys = {} # Maybe just change to a list?
        self.monkeys = []
        self.lives = 200
        self.cash = 800
        self.priceList = priceList
        self.upgradeList = upgradeList

        self.SmGrid = []
        self.MeGrid = []
        self.subGrid = [] # Not used yet
        self.pirGrid = [] # Not used yet
        self.LaGrid = []
        self.AcGrid = []
        self.HeGrid = []
        self.FaGrid = [] # Not used yet
    
    def availUpgrades(self, cash):
        uList = []
        for m in self.monkeys: # Iterate through all the monkeys we have set down
            up = m.upgrades
            i = m.PUindex
            for j in range(2): # Iterate through all possible upgrades
                if not up[j] == None: # Check that it is not an impossible upgrade
                    k = up[j] + 1
                    if self.upgradeList[i][j][k] <= cash: # Check that we can afford it
                        z = (m, j)
                        uList.append(z)
        return uList
    
    def availPlacement(self, cash):
        pList = []
        for puInd in range(len(self.priceList)): 
            if self.priceList[puInd] <= cash: # Just check what monkeys we have money for
                pList.append(puInd)
        return pList
    
    def upgradeM(self, monkey, index):
        if not self.upgrades[index] == None:
            upgrade(index, monkey.position)
            monkey.upgrades[index] += 1
            self.cash -= self.upgradeList[monkey.PUindex][index][monkey.upgrades[index]]
            if monkey.upgrades[0] >= 1 and monkey.upgrades[1] >= 1:
                monkey.upgrades[2] = None
            if monkey.upgrades[1] >= 1 and monkey.upgrades[2] >= 1:
                monkey.upgrades[0] = None
            if monkey.upgrades[0] >= 1 and monkey.upgrades[2] >= 1:
                monkey.upgrades[1] = None

    def placeM(self, position, puIndex):
        setMonkey(puIndex, position)
        if grid.findRed(position) == None:
            m = Monkey(position, puIndex)
            self.monkeys.append(m)
            self.removeSpaces(position, puIndex)
            self.cash -= self.priceList[puIndex]
        else:
            print("UH OH")
            return None

    def removeSpaces(self, position, index):
        x = position[0]
        y = position[1]
        if index == 1 or index == 4 or index ==  5 or index == 6 or index == 7 or index == 16 or index == 17: # Small Monkeys
            for i in range(len(self.SmGrid)):
                if self.SmGrid[i][0] <= x + 66 and self.SmGrid[i][0] >= x - 66 and self.SmGrid[i][1] <= y + 59 and self.SmGrid[i][1] >= y - 59:
                    self.SmGrid.pop(i)
            for j in range(len(self.MeGrid)):
                if self.MeGrid[j][0] <= x + 66 and self.MeGrid[j][0] >= x - 66 and self.MeGrid[j][1] <= y + 59 and self.MeGrid[j][1] >= y - 59:
                    self.MeGrid.pop(j)
            for k in range(len(self.LaGrid)):
                if self.LaGrid[k][0] <= x + 66 and self.LaGrid[k][0] >= x - 66 and self.LaGrid[k][1] <= y + 59 and self.LaGrid[k][1] >= y - 59:
                    self.LaGrid.pop(k)
            for m in range(len(self.AcGrid)):
                if self.AcGrid[m][0] <= x + 66 and self.AcGrid[m][0] >= x - 66 and self.AcGrid[m][1] <= y + 59 and self.AcGrid[m][1] >= y - 59:
                    self.AcGrid.pop(m)
            for n in range(len(self.HeGrid)):
                if self.HeGrid[n][0] <= x + 66 and self.HeGrid[n][0] >= x - 66 and self.HeGrid[n][1] <= y + 59 and self.HeGrid[n][1] >= y - 59:
                    self.HeGrid.pop(n)
        if index == 2 or index == 3 or index ==  13 or index == 14 or index == 18 or index == 22 or index == 0: # Medium Monkeys
            for i in range(len(self.SmGrid)):
                if self.SmGrid[i][0] <= x + 77 and self.SmGrid[i][0] >= x - 77 and self.SmGrid[i][1] <= y + 67 and self.SmGrid[i][1] >= y - 67:
                    self.SmGrid.pop(i)
            for j in range(len(self.MeGrid)):
                if self.MeGrid[j][0] <= x + 77 and self.MeGrid[j][0] >= x - 77 and self.MeGrid[j][1] <= y + 67 and self.MeGrid[j][1] >= y - 67:
                    self.MeGrid.pop(j)
            for k in range(len(self.LaGrid)):
                if self.LaGrid[k][0] <= x + 77 and self.LaGrid[k][0] >= x - 77 and self.LaGrid[k][1] <= y + 67 and self.LaGrid[k][1] >= y - 67:
                    self.LaGrid.pop(k)
            for m in range(len(self.AcGrid)):
                if self.AcGrid[m][0] <= x + 77 and self.AcGrid[m][0] >= x - 77 and self.AcGrid[m][1] <= y + 67 and self.AcGrid[m][1] >= y - 67:
                    self.AcGrid.pop(m)
            for n in range(len(self.HeGrid)):
                if self.HeGrid[n][0] <= x + 77 and self.HeGrid[n][0] >= x - 77 and self.HeGrid[n][1] <= y + 67 and self.HeGrid[n][1] >= y - 67:
                    self.HeGrid.pop(n)
        if index == 20: # Large Monkeys
            for i in range(len(self.SmGrid)):
                if self.SmGrid[i][0] <= x + 87 and self.SmGrid[i][0] >= x - 87 and self.SmGrid[i][1] <= y + 75 and self.SmGrid[i][1] >= y - 75:
                    self.SmGrid.pop(i)
            for j in range(len(self.MeGrid)):
                if self.MeGrid[j][0] <= x + 87 and self.MeGrid[j][0] >= x - 87 and self.MeGrid[j][1] <= y + 75 and self.MeGrid[j][1] >= y - 75:
                    self.MeGrid.pop(j)
            for k in range(len(self.LaGrid)):
                if self.LaGrid[k][0] <= x + 87 and self.LaGrid[k][0] >= x - 87 and self.LaGrid[k][1] <= y + 75 and self.LaGrid[k][1] >= y - 75:
                    self.LaGrid.pop(k)
            for m in range(len(self.AcGrid)):
                if self.AcGrid[m][0] <= x + 87 and self.AcGrid[m][0] >= x - 87 and self.AcGrid[m][1] <= y + 75 and self.AcGrid[m][1] >= y - 75:
                    self.AcGrid.pop(m)
            for n in range(len(self.HeGrid)):
                if self.HeGrid[n][0] <= x + 87 and self.HeGrid[n][0] >= x - 87 and self.HeGrid[n][1] <= y + 75 and self.HeGrid[n][1] >= y - 75:
                    self.HeGrid.pop(n)
        if index == 10: # Ace Monkeys
            for i in range(len(self.SmGrid)):
                if self.SmGrid[i][0] <= x + 152 and self.SmGrid[i][0] >= x - 152 and self.SmGrid[i][1] <= y + 85 and self.SmGrid[i][1] >= y - 85:
                    self.SmGrid.pop(i)
            for j in range(len(self.MeGrid)):
                if self.MeGrid[j][0] <= x + 152 and self.MeGrid[j][0] >= x - 152 and self.MeGrid[j][1] <= y + 85 and self.MeGrid[j][1] >= y - 85:
                    self.MeGrid.pop(j)
            for k in range(len(self.LaGrid)):
                if self.LaGrid[k][0] <= x + 152 and self.LaGrid[k][0] >= x - 152 and self.LaGrid[k][1] <= y + 85 and self.LaGrid[k][1] >= y - 85:
                    self.LaGrid.pop(k)
            for m in range(len(self.AcGrid)):
                if self.AcGrid[m][0] <= x + 152 and self.AcGrid[m][0] >= x - 152 and self.AcGrid[m][1] <= y + 85 and self.AcGrid[m][1] >= y - 85:
                    self.AcGrid.pop(m)
            for n in range(len(self.HeGrid)):
                if self.HeGrid[n][0] <= x + 152 and self.HeGrid[n][0] >= x - 152 and self.HeGrid[n][1] <= y + 85 and self.HeGrid[n][1] >= y - 85:
                    self.HeGrid.pop(n)
        if index == 11: # Heli Monkeys
            for i in range(len(self.SmGrid)):
                if self.SmGrid[i][0] <= x + 146 and self.SmGrid[i][0] >= x - 146 and self.SmGrid[i][1] <= y + 127 and self.SmGrid[i][1] >= y - 127:
                    self.SmGrid.pop(i)
            for j in range(len(self.MeGrid)):
                if self.MeGrid[j][0] <= x + 146 and self.MeGrid[j][0] >= x - 146 and self.MeGrid[j][1] <= y + 127 and self.MeGrid[j][1] >= y - 127:
                    self.MeGrid.pop(j)
            for k in range(len(self.LaGrid)):
                if self.LaGrid[k][0] <= x + 146 and self.LaGrid[k][0] >= x - 146 and self.LaGrid[k][1] <= y + 127 and self.LaGrid[k][1] >= y - 127:
                    self.LaGrid.pop(k)
            for m in range(len(self.AcGrid)):
                if self.AcGrid[m][0] <= x + 146 and self.AcGrid[m][0] >= x - 146 and self.AcGrid[m][1] <= y + 127 and self.AcGrid[m][1] >= y - 127:
                    self.AcGrid.pop(m)
            for n in range(len(self.HeGrid)):
                if self.HeGrid[n][0] <= x + 146 and self.HeGrid[n][0] >= x - 146 and self.HeGrid[n][1] <= y + 127 and self.HeGrid[n][1] >= y - 127:
                    self.HeGrid.pop(n)

##################################### MAIN #####################################

def main():
    smL = []
    meL = []
    laL = []
    acL = []
    heL = []
    pL = priceListEasy()
    uL = upgradeListEasy()
    Player1 = Player(pL, uL)
    with open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMSm.txt", "r") as fSm:
        line = fSm.readline()
        while(line != "\n"):
            l = line.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").split(",")
            p = (int(l[0]), int(l[1]))
            smL.append(p)
            line = fSm.readline()
    with open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMMe.txt", "r") as fMe:
        line = fMe.readline()
        while(line != "\n"):
            l = line.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").split(",")
            p = (int(l[0]), int(l[1]))
            meL.append(p)
            line = fMe.readline()
    with open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMLa.txt", "r") as fLa:
        line = fLa.readline()
        while(line != "\n"):
            l = line.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").split(",")
            p = (int(l[0]), int(l[1]))
            laL.append(p)
            line = fLa.readline()
    with open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMAc.txt", "r") as fAc:
        line = fAc.readline()
        while(line != "\n"):
            l = line.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").split(",")
            p = (int(l[0]), int(l[1]))
            acL.append(p)
            line = fAc.readline()
    with open(r"C:\Users\maxwi\Documents\GitHub\BTD6-AI\MMHe.txt", "r") as fHe:
        line = fHe.readline()
        while(line != "\n"):
            l = line.replace("(", "").replace(")", "").replace("\n", "").replace(" ", "").split(",")
            p = (int(l[0]), int(l[1]))
            heL.append(p)
            line = fHe.readline()
    Player1.SmGrid = smL
    Player1.MeGrid = meL
    Player1.LaGrid = laL
    Player1.AcGrid = acL
    Player1.HeGrid = heL
    return 0

if __name__ == "__main__":
    main()