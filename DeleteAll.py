import time
from tools import *

def pipeline():
    while True:
        index = objectMatch(getScreenShot(), cv.imread('Pic/item.png'))
        if len(index) == 0:
            break
        index = index[0]
        clickMouseButton(index[0], index[1], "Right")
        time.sleep(0.5)

        index = objectMatch(getScreenShot(), cv.imread("Pic/trashBin.png"))[0]
        clickMouseButton(index[0], index[1], "Left")
        time.sleep(0.5)

        index = objectMatch(getScreenShot(), cv.imread("Pic/delete.png"))[0]
        clickMouseButton(index[0], index[1], "Left")
        time.sleep(0.5)
        
    pag.alert("已完成")
pipeline()
