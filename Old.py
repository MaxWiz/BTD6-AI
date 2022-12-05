import pyautogui
import time
from pynput.keyboard import Key, Controller
import numpy
import operator

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

def oldMain(): # Old code that was removed from main
            # r1 = random.randint(0, len(availP)) # Generate a random number that is within the range of the placement options
            # if len(availP) != 0:
            #     print("Out of " + str(len(availP)) + " placement options, it chose " + str(r1-1) + " which is at " + str(availP[r1-1][0]) + ". Place was " + str(n1 == 1) + " and cash was: " + str(Player1.cash))
            # if (len(availP) != 0 and n1 == 1) or roundNum == 1: # We always want to place a tower on round 1, obviously
            #     s1 = availP[r1-1]
            #     Player1.placeM(s1[0], s1[1])
            #     mTest = Monkey(s1[0], s1[1])
            #     print("It placed " + str(mTest.name) + " at: " + str(s1[0]))
            
            # cash = Player1.cash # Set cash so that we have the correct amount for upgrades, this could likely be handled inside the Player class
            
            # availU = Player1.availUpgrades(Player1.cash) # Generate the available upgrades, AFTER placement
            # r2 = random.randint(0, len(availU)) # Generate a random number that is within the range of the upgrade options
            # print("Out of " + str(len(availU)) + " upgrade options, it chose " + str(r2) + ". Upgrade was " + str(n2 == 1) + " and cash was: " + str(Player1.cash))
            # # print("Avail U:" + str(availU))
            # if len(availU) != 0 and n2 == 1:
            #     s2 = availU[r2-1]
            #     Player1.upgradeM(s2[0], s2[1])
            #     print("Upgraded " + str(s2[0].name) + " at " + str(s2[0].position) + " to " + str(s2[0].upgrades[0]) + str(s2[0].upgrades[1]) + str(s2[0].upgrades[2]))
    return 0