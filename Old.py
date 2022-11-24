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