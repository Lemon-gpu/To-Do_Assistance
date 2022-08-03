from tools import *
import pyautogui as pag
import time

def pipeline():
    while True:
        index: list = objectMatch(getScreenShot(), cv.imread('Pic/circle.png'))
        if len(index) == 0:
            break
        index = index[0]
        clickMouseButton(index[0], index[1], "Right", 2)
        time.sleep(0.5)
        
        trashBinIndex = objectMatch(getScreenShot(), cv.imread("Pic/trashBin.png"))[0]
        clickMouseButton(trashBinIndex[0], trashBinIndex[1], "Left", 2)
        time.sleep(0.5)

        deleteIndex = objectMatch(getScreenShot(), cv.imread("Pic/delete.png"))[0]
        clickMouseButton(deleteIndex[0], deleteIndex[1], "Left", 1)
        time.sleep(0.5)

pipeline()



